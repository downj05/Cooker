from helpers import click_image, focus_unturned, is_unturned_running, kill_unturned, move_mouse_delta, turn_mouse
import steam_helpers
import pyautogui as py
import time
from PyQt5.QtCore import QThread, pyqtSignal
import log_reader
from random import randint, choice


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


    def __init__(self, address, port, password=None, overlay=None, retries=3):
        super().__init__()
        self.address = address
        self.port = port
        self.password = password
        self.overlay = overlay
        self.retries = retries
        print("JoinServerThread: init")
    
    
    def run(self):
        for i in range(self.retries):
            try:
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
                print("JoinServerThread: Client is connecting to server")
                print("JoinServerThread: User is loading assets etc")
                self.loading_assets.emit()

                print("JoinServerThread: game functions match:", log_reader.wait_for_pattern(r"Ready to connect").group())
                print("JoinServerThread: Assets loaded! Client performing authentication with server!")
                print("JoinServerThread: game functions match:", log_reader.wait_for_pattern(r"Accepted by server").group())
                print("JoinServerThread: Client authenticated with server!")
                print("JoinServerThread: Client is initializing battle eye")
                print("JoinServerThread: game functions match:", log_reader.wait_for_pattern(r"BattlEye client message: Initialized").group())
                print("JoinServerThread: Client initialized battle eye!")
                print("JoinServerThread: Client has joined the server!")
                self.joined_server.emit()
                return
            except Exception as e:
                print(f"JoinServerThread: error during server join! : {e}")
                print(f"JoinServerThread: trying it again! ({i}/{self.retries}) retries")
                time.sleep(1)
                continue

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
def micro_movements():
    time.sleep(randint(1,5))
    c = choice(['wiggle', 'mouse', 'inventory'])
    if c is 'wiggle':
        # Random wiggle
        c = choice(['q', 'e'])
        py.keyDown(c)
        time.sleep(0.05)
        py.keyUp(c)
        return
    if c is 'mouse':
        # Random mouse movement
        x = randint(-20, 20)
        y = randint(-5, 5)
        move_mouse_delta(x, y)
        return
    if c is 'inventory':
        # Open inventory
        py.press("g")
        time.sleep(randint(1, 6))
        # Close inventory
        py.press("g")
        return


def random_walk():
    forward = 'w'
    py.keyUp(forward)
    time.sleep(randint(1,8))
    py.keyDown(forward)
    turn_mouse(randint(-800, 800), randint(-50, 50), 6)
    time.sleep(randint(1,8))
    return

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

@focus_unturned
def escape_key():
    print("game_functions.escape_key: pressing escape key")
    py.press("esc")

@focus_unturned
def send_message(msg: str):
    print("game_functions.send_message: sending message: ", msg)
    py.press("l")
    time.sleep(0.5)
    py.write(msg)
    py.press("enter")

if __name__ == '__main__':
    for _ in range(2):
        time.sleep(1)
    print('starting')
    while True:
        random_walk()