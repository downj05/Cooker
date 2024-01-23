from gui_loading import Ui_MainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtCore import QThread

from multiprocessing import Process, Queue
from PyQt5.QtCore import QObject, pyqtSignal

class GuiLogic(Ui_MainWindow):


    def __init__(self, app):
        super().__init__()
        self.setupUi(app)
        # Set window title
        app.setWindowTitle("Cooker Loading...")
        app.setWindowFlags(Qt.FramelessWindowHint)
        app.setWindowIcon(QIcon('design\Company_Logo.ico'))
        

        # load the loading gif
        from PyQt5.QtGui import QMovie
        movie = QMovie('design\spinner.gif')
        self.loadingGifLabel.setMovie(movie)
        movie.start()

    def load(self, progress: int, status: str):
        self.loadingBar.setValue(progress)
        self.loadingStatusLabel.setText(status)




if __name__ == "__main__":
        from PyQt5.QtWidgets import QApplication, QMainWindow
        from qt_material import apply_stylesheet
        from random import choice
        import string
        import ctypes
        from sys import argv, exit
        myappid = f'company.cooker.{"".join([choice([choice(string.ascii_lowercase), choice(string.digits)]) for c in range(16)])}' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        app = QApplication(argv)
        extra = {
        'font_family': 'Roboto',
        'font_size': '10px',
        'line_height': '13px',
        # Density Scale
        'density_scale': '-1',
    }
        apply_stylesheet(app, theme='pink.xml', extra=extra, )

        LoadingWindow = QMainWindow()
        ui = GuiLogic(LoadingWindow)
        LoadingWindow.show()
        # Center the window
        LoadingWindow.move(QDesktopWidget().availableGeometry().center() - LoadingWindow.rect().center())
        exit(app.exec_())