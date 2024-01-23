from helpers import click_image, focus_unturned, is_unturned_running, kill_unturned
import steam_helpers
import pyautogui as py
import time
from PyQt5.QtCore import QThread, pyqtSignal
import log_reader


def launch_unturned(wait_for_menu=False,**kwargs):
    # State: [unturned process detected, main menu loaded]
    print("WARNING: THIS FUNCTION IS DEPRECATED, USE LaunchUnturnedThread INSTEAD!! :D")
    state = kwargs.get("state", [False, False])

    print("launching unturned")
    
    steam_helpers.launch_steam_game(steam_helpers.UNTURNED_APP_ID)
    while not is_unturned_running(): # wait for unturned to launch
        time.sleep(0.1)
    # Unturned process has been detected
    state[0] = True
    print("unturned process detected")
    if not wait_for_menu:
        return
    # Wait for main menu to load
    log_reader.wait_for_pattern(r"Menu UI ready")
    state[1] = True
    print("main menu loaded")
    return state

class LaunchUnturnedThread(QThread):
    process_started = pyqtSignal()
    menu_loaded = pyqtSignal()

    def __init__(self, wait_for_menu=False):
        super().__init__()
        self.wait_for_menu = wait_for_menu
    
    def run(self):
        print("LaunchUnturnedThread.run: launching unturned")
        steam_helpers.launch_steam_game(steam_helpers.UNTURNED_APP_ID)
        while not is_unturned_running(): # wait for unturned to launch
            print(f"LaunchUnturnedThread.run: waiting for unturned to launch, is_unturned_running: {is_unturned_running()} is False")
            time.sleep(0.1)
        # Unturned process has been detected
        self.process_started.emit()
        print("LaunchUnturnedThread.run: unturned process detected")
        if not self.wait_for_menu:
            return
        # Wait for main menu to load
        log_reader.wait_for_pattern(r"Menu UI ready")
        self.menu_loaded.emit()
        print("LaunchUnturnedThread.run: main menu loaded")
        return

class JoinServerThread(QThread):

    loading_assets = pyqtSignal()
    joined_server = pyqtSignal()


    def __init__(self, address, port, password=None, overlay=None):
        super().__init__()
        self.address = address
        self.port = port
        self.password = password
        self.overlay = overlay
        print("JoinServerThread: init")
    
    
    def run(self):
            print("JoinServerThread: Joining server with address: ", self.address, ":", self.port, " password: ", self.password[:2] + "*" * len(self.password[2:]))
            click_image("menu_play.png", press_key_on_fail="esc", confidence=0.9)
            click_image("connect_ip.png", confidence=0.9)
            click_image("ip_field.png", x_offset=-200)
            py.write(self.address)
            click_image("port_field.png", x_offset=-200)
            py.write(str(self.port))
            if self.password is not None:
                click_image("password_field.png", x_offset=-100, confidence=0.7)
                py.write(self.password)
            click_image("ip_connect_button.png", confidence=0.7)
            click_image("join_button.png", confidence=0.75)
            print("Client is connecting to server")
            print("User is loading assets etc")
            self.loading_assets.emit()

            print("game functions match:", log_reader.wait_for_pattern(r"Ready to connect").group())
            print("Assets loaded! Client performing authentication with server!")
            print("game functions match:", log_reader.wait_for_pattern(r"Accepted by server").group())
            print("Client authenticated with server!")
            print("Client is initializing battle eye")
            print("game functions match:", log_reader.wait_for_pattern(r"BattlEye client message: Initialized").group())
            print("Client initialized battle eye!")
            print("Client has joined the server!")
            self.joined_server.emit()

@focus_unturned
def frank_b_oogie(loop=False):
    while True:
        py.keyDown("q")
        # Go Down
        py.press("z")
        time.sleep(0.2)
        # Go up
        py.press("z")
        py.keyUp("q")
        time.sleep(0.05)
        py.keyDown("e")
        py.press("z")
        time.sleep(0.2)
        py.press("z")
        py.keyUp("e")
        if not loop:
            break

@focus_unturned
def join_server(address, port, password=None, overlay=None):
    print("WARNING: THIS FUNCTION IS DEPRECATED, USE JoinServerThread INSTEAD!! :D")
    print("Joining server with address: ", address, ":", port, " password: ", password[:2] + "*" * len(password[2:]))
    click_image("menu_play.png", press_key_on_fail="esc", confidence=0.9)
    click_image("connect_ip.png", confidence=0.6)
    click_image("ip_field.png", x_offset=-200)
    py.write(address)
    click_image("port_field.png", x_offset=-200)
    py.write(str(port))
    if password is not None:
        click_image("password_field.png", x_offset=-100, confidence=0.7)
        py.write(password)
    click_image("ip_connect_button.png", confidence=0.7)
    click_image("join_button.png", confidence=0.75)
    print("Client is connecting to server")
    print("User is loading assets etc")
    print("game functions match:", log_reader.wait_for_pattern(r"Ready to connect").group())
    print("Assets loaded! Client performing authentication with server!")
    print("game functions match:", log_reader.wait_for_pattern(r"Accepted by server").group())
    print("Client authenticated with server!")
    print("Client is initializing battle eye")
    print("game functions match:", log_reader.wait_for_pattern(r"BattlEye client message: Initialized").group())
    print("Client initialized battle eye!")
    print("Client has joined the server!")

if __name__ == '__main__':
    time.sleep(2)
    frank_b_oogie()