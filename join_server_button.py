from PyQt5.QtCore import QThread, pyqtSignal, QObject, QEventLoop
from PyQt5.QtWidgets import QPushButton
import log_reader
from gui import Ui_MainWindow
import game_functions as game
import time
import helpers

class JoinButtonLogic(QObject):
    def __init__(self, button: QPushButton, window: Ui_MainWindow):
        super().__init__()
        print(f"JoinButtonLogic: init, {window.serverIP.text()}")
        self.button = button
        self.window = window
    
        self.button.clicked.connect(self.buttonPressed)

    def buttonPressed(self):
        if not game.is_unturned_running():
            print("JoinButtonLogic.buttonPressed: unturned not running, starting")
            self.window.startGame.click()
            print("buttonPressed: loaded in")

        if log_reader.is_in_game():
            print("JoinButtonLogic.buttonPressed: in game already!, skipping join logic")
            self.window.loading_assets = True
            self.window.joined_server = True
            print("JoinButtonLogic.buttonPressed: finished")
            return
        
        print("JoinButtonLogic.buttonPressed: joining server")
        t = game.JoinServerThread(
            self.window.serverIP.text(),
            self.window.serverPort.text(),
            self.window.serverPassword.text()
        )
        t.start()

        # wait for server asset signal
        print("JoinButtonLogic.buttonPressed: waiting for server assets to start loading (bot will be clicking through the main menu)")
        loop = QEventLoop()
        t.loading_assets.connect(loop.quit)
        loop.exec_()
        self.window.loading_assets = t.loading_assets
        print(f"JoinButtonLogic.buttonPressed: window.loading_assets:{self.window.loading_assets} t.loading_assets:{t.loading_assets}")



        # wait for joined server signal
        print("JoinButtonLogic.buttonPressed: waiting to load into server")
        loop = QEventLoop()
        t.joined_server.connect(loop.quit)
        loop.exec_()
        self.window.joined_server = t.joined_server
        print(f"JoinButtonLogic.buttonPressed: window.joined_server:{self.window.joined_server} t.joined_server:{t.joined_server}")

        print("JoinButtonLogic.buttonPressed: finished")
        return