from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import time


class OverlayWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.X11BypassWindowManagerHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setGeometry(QtWidgets.QDesktopWidget().screenGeometry())
        self.dots = []
        self.images = []
        self.shapes = []
        self.gifs = []

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.red))
        for dot, size in self.dots:
            painter.drawEllipse(dot, size, size)
        for image, rect in self.images:
            painter.drawImage(rect, image)
        for shape in self.shapes:
            painter.drawPath(shape)
        for movie, rect in self.gifs:
            image = movie.currentImage()
            painter.drawImage(rect, image)

    def play_gif(self, gif_path, x, y, width, height, duration=None, looping=True, loops=0):
        movie = QtGui.QMovie(gif_path)
        rect = QtCore.QRectF(x, y, width, height)
        self.gifs.append((movie, rect))
        if not looping:
            loop_counter = [loops]
            def stop_after_loops():
                loop_counter[0] -= 1
                if loop_counter[0] <= 0:
                    movie.stop()
            movie.finished.connect(stop_after_loops)
        movie.start()
        movie.frameChanged.connect(self.update)
        if duration is not None:
            QtCore.QTimer.singleShot(duration * 1000, self.clear)

    def clear(self):
        for movie, _ in self.gifs:
            movie.stop()
        self.gifs.clear()
        self.update()

    def draw_image(self, image_path, x, y, width, height, duration=1):
        image = QtGui.QImage(image_path)
        rect = QtCore.QRectF(x, y, width, height)
        self.images.append((image, rect))
        self.update()
        if duration is not None:
            QtCore.QTimer.singleShot(duration * 1000, lambda: self.clear_image(image))

    def clear_image(self, image):
        self.images = [(img, rect) for img, rect in self.images if img != image]
        self.update()

    def draw_shape(self, shape):
        self.shapes.append(shape)
        self.update()

    def draw_dot(self, x, y, duration, size=2.5):
        self.dots.append((QtCore.QPointF(x, y), size))
        self.update()
        QtCore.QTimer.singleShot(duration * 1000, self.clear_dots)

    def clear_dots(self):
        self.dots.clear()
        self.update()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.ActivationChange:
            if self.isActiveWindow():
                self.setWindowOpacity(1.0)
            else:
                self.setWindowOpacity(0.0)

class DrawDotThread(QThread):
    drawDot = pyqtSignal(int, int, int)

    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay
        self.drawDot.connect(self.overlay.draw_dot)

    def run(self):
        # Replace this with your own logic for when and where to draw dots
        while True:
            self.drawDot.emit(100, 100, 5)  # Draw a dot at (100, 100) for 5 seconds
            time.sleep(5)