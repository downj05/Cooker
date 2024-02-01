
from PyQt5 import QtWidgets, QtGui, QtCore
from gui import Ui_MainWindow
import save_widgets
import traceback
from info_tab import init_info_tab
import qdarkstyle
import game_functions as game
from os import path
import webhook
import time
import helpers
from start_unturned_button import GameButtonLogic
from join_server_button import JoinButtonLogic
import random
from string import ascii_lowercase, digits
from ui_helpers import show_message, input_dialog
from server_combo import ServerComboBoxLogic
from start_cooker_button import StartCookerButtonLogic


ICON_PATH = path.join('design', 'icons', 'Company_Logo.ico')

def not_implemented(parent):
    show_message(parent, "Error", "Not implemented yet")

def test(e):
    print(e.__dict__, type(e))

class GuiLogic(Ui_MainWindow):
    def __init__(self, app):
        print("GuiLogic: init")
        super().__init__()
        self.setupUi(app)
        # Set window title
        app.setWindowTitle("Smuggler Suite Cooker")
        # Set window flags
        # QtCore.Qt.WindowStaysOnTopHint
        app.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set icon
        app.setWindowIcon(QtGui.QIcon(ICON_PATH))
    

        # Set up custom window bar logic
        # Dragging variables
        self.m_drag = False
        self.m_DragPosition = QtCore.QPoint()

        # Game state
        self.unturned_running = False
        self.menu_loaded = False
        self.joined_server = False


        # Override windowBar events
        self.windowBar.mouseMoveEvent = self.customMouseMoveEvent
        self.windowBar.mousePressEvent = self.customMousePressEvent
        self.windowBar.mouseReleaseEvent = self.customMouseReleaseEvent
        
        # Assign windowBar buttons
        self.closeButton.clicked.connect(self.btn_close_clicked)
        self.minimizeButton.clicked.connect(self.btn_min_clicked)

        # Set up the game button logic (Unturned starting/stopping)
        self.gameButtonLogic = GameButtonLogic(self.startGame, self)

        # Set up slider logic
        self.slider_update_label_taken_dict = {}
        self.slider_update_label(self.cookTimeSlider, self.cookTimeLabelTime)
        self.slider_update_label(self.webhookPeriodicIntervalSlider, self.webhookPeriodicIntervalLabel)



        # Server settings
        save_widgets.init(self.serverIP)
        save_widgets.init(self.serverPort)
        save_widgets.init(self.serverPassword)

        # Join button
        self.joinServerButtonLogic = JoinButtonLogic(self.joinServerButton, self)

        # Cooker settings
        save_widgets.init(self.cookTimeSlider)
        save_widgets.init(self.rejoinLimit)
        
        # Webhook settings
        save_widgets.init(self.webhookEnabledCheckBox)
        save_widgets.init(self.webhookUrlTextBox)
        save_widgets.init(self.webhookPostPeriodicCheckBox)
        save_widgets.init(self.webhookPeriodicIntervalSlider)

        # Set up server combo box logic
        self.serverComboBoxLogic = ServerComboBoxLogic(self.saveServerButton, self.updateServerButton, self.deleteServerButton, self.serverComboBox, self.serverIP, self.serverPort, self.serverPassword)
        save_widgets.init(self.serverComboBox)
        
        
        # Set up cooker button logic
        self.startCookerButtonLogic = StartCookerButtonLogic(self.startCooker, self)

        # Webhook test button
        self.testWebhookButton.clicked.connect(self.webhookTest)

        # Experiments

        save_widgets.init(self.joinEscapeKeyCheckboxGroup)
        save_widgets.init(self.joinEscapeKeyTime)
        
        save_widgets.init(self.antiAfkMethodComboBox)

        save_widgets.init(self.joinCommandBox)
        save_widgets.init(self.commandOnJoinTextField)

        save_widgets.init(self.periodicStatusCommandGroupCheckBox)
        save_widgets.init(self.periodicCommandTextField)

        save_widgets.init(self.loopCookCheckbox)
        save_widgets.init(self.loopSpinBox)

        # Info

        # Set up device info logic
        self.system_info_thread = init_info_tab(self.cpuTxt, self.ramTxt, self.hostnameTxt, self.steam64Txt, self.steamUsernameTxt)


    def slider_update_label(self, slider: QtWidgets.QSlider, label: QtWidgets.QLabel):
        def _update():
            label.setText(helpers.seconds_to_hms(int(slider.value())))
            if slider.objectName in self.slider_update_label_taken_dict:
                self.slider_update_label_taken_dict[slider.objectName] = False
                return
        slider.valueChanged.connect(_update)

        # If lable is a text box, update the slider when the text box is changed
        # Use a helper function to convert the hms (e.g 3h20s) to seconds
        if isinstance(label, QtWidgets.QLineEdit):
            def _update_slider():
                self.slider_update_label_taken_dict[slider.objectName] = True
                slider.setValue(helpers.hms_to_seconds(label.text()))
            label.textChanged.connect(_update_slider)



    def webhookTest(self):
        print(f"Unturned running: {self.unturned_running}, Menu loaded: {self.menu_loaded}, Game joined: {self.joined_server}")
        try:
            w = webhook.Webhook(self.webhookUrlTextBox.text(), self.steam64Txt.text(), self.steamUsernameTxt.text())
            w.test()
            show_message(self.testWebhookButton, "Success", "Webhook sent successfully")

            # Focus GUI
        except Exception as e:
            show_message(self.testWebhookButton, "Error", f"Failed to send webhook\n{e}")
            return


    # Custom window bar mouse dragging implementation
    def customMousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - MainWindow.pos()
            event.accept()

    def customMouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.m_drag:
            MainWindow.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    def customMouseReleaseEvent(self, event):
        self.m_drag = False
    
    def btn_close_clicked(self):
        MainWindow.close()

    def btn_min_clicked(self):
        MainWindow.showMinimized()


if __name__ == "__main__":
    print("main: init")
    import sys, ctypes

    
    print("main: create app")
    app = QtWidgets.QApplication(sys.argv)

    print("main: set app id")
    myappid = f'company.cooker.{"".join([random.choice([random.choice(ascii_lowercase), random.choice(digits)]) for c in range(16)])}' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    extra = {
    'font_family': 'Roboto',
    'font_size': '10px',
    'line_height': '13px',
    # Density Scale
    'density_scale': '-1',
}
    # apply_stylesheet(app, theme='pink.xml', extra=extra, )
    print("main: apply stylesheet")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    print("main: create main window")
    MainWindow = QtWidgets.QMainWindow()
    print("main: create gui logic")
    ui = GuiLogic(MainWindow)
    print("main: show main window")
    MainWindow.show()
    sys.exit(app.exec_())
