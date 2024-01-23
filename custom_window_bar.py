import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint


class CustomWindowBar(QWidget):
    def __init__(self, bar, *args, **kwargs):
        super().__init__(bar, *args, **kwargs)
        print(self.objectName())

    #     self.closeButton = closeButton
    #     self.minimizeButton = minimizeButton

    #     # Button events
    #     self.closeButton.clicked.connect(self.btn_close_clicked)
    #     self.minimizeButton.clicked.connect(self.btn_min_clicked)

    #     # For dragging
    #     self.m_drag = False
    #     self.m_DragPosition = QPoint()

    def mousePressEvent(self, event):
        print(f"presed! {event}, {type(event)}")
        # if event.button() == Qt.LeftButton:
        #     self.m_drag = True
        #     self.m_DragPosition = event.globalPos() - self.pos()
        #     event.accept()

    def mouseMoveEvent(self, event):
        print(f"presed! {event}, {type(event)}")
        if event.buttons() == Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False


    # def btn_close_clicked(self):
    #     self.parent.close()

    # def btn_max_clicked(self):
    #     self.parent.showMaximized()

    # def btn_min_clicked(self):
    #     self.parent.showMinimized()