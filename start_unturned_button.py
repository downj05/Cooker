from PyQt5.QtCore import QThread, pyqtSignal, QObject, QEventLoop
import game_functions as game
import time
from os import system
from gui import Ui_MainWindow
from PyQt5 import QtWidgets

class MonitorThread(QThread):
    statusChanged = pyqtSignal(bool)
    def run(self):
        while True:
            is_running = game.is_unturned_running()
            self.statusChanged.emit(is_running)
            time.sleep(4)

class KillUnturnedThread(QThread):
    killed = pyqtSignal()

    def run(self):
        game.kill_unturned()
        self.killed.emit()

class GameButtonLogic(QObject):
    def __init__(self, button, window: Ui_MainWindow):
        super().__init__()
        print(f"GameButtonLogic: init, {window.serverIP.text()}")
        assert isinstance(button, QtWidgets.QPushButton)
        self.window = window
        self.button = button
        self.button.clicked.connect(self.buttonPressed)

        self.monitorThread = MonitorThread()
        self.monitorThread.statusChanged.connect(self.update_button_state)

        print("GameButtonLogic: starting monitor thread")
        self.monitorThread.start()

        self.startThread = None

    def buttonPressed(self, state):
        # Starting unturned
        if state is True:
            print("buttonPressed: starting unturned")
            self.button.setEnabled(False)
            self.button.setText('Starting Unturned')
            self.startThread = game.LaunchUnturnedThread(wait_for_menu=True)
            self.startThread.start()

            # Wait for unturned to start
            print("buttonPressed: waiting for unturned to start")
            loop = QEventLoop()
            self.startThread.process_started.connect(loop.quit)
            loop.exec_()

            self.button.setEnabled(True)
            print("buttonPressed: unturned loading")
            # Wait for main menu to load
            loop = QEventLoop()
            self.startThread.menu_loaded.connect(loop.quit)
            loop.exec_()

            # Update menu loaded state in window
            self.window.menu_loaded = True

            print("buttonPressed: unturned started, main menu loaded")

        # Stopping unturned
        else:
            if isinstance(self.startThread, game.LaunchUnturnedThread):
                self.startThread.terminate()
                self.startThread.wait()
                self.startThread = None
            print("buttonPressed: killing unturned")
            game.kill_unturned()
        
        self.update_button_state(state)

    def update_button_state(self, is_running: bool):
        # Update unturned running state in window
        if self.window.unturned_running != is_running:
            # Post update
            print(f"update_button_state: updating unturned_running state in window {self.window.unturned_running} -> {is_running}")
        self.window.unturned_running = is_running

        # Stopping unturned
        if is_running:
            self.button.setText('Kill Unturned')
            self.button.setChecked(True)
        # Starting unturned
        else:
            # If unturned is closed, menu and game joined are automatically false
            self.window.menu_loaded = False
            self.window.joined_server = False
            self.button.setText('Start Unturned')
            self.button.setChecked(False)