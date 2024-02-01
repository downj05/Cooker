import pyautogui as py
from pywinauto import Application
import time
import os.path as pth
import os
import psutil
import socket
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QLineEdit
from win32api import mouse_event
from win32con import MOUSEEVENTF_MOVE
from typing import Tuple, Union
from win32gui import SetForegroundWindow, FindWindow, GetWindowText, EnumWindows, GetWindowRect, BringWindowToTop, ShowWindow
from win32process import GetWindowThreadProcessId
from overlay_window import OverlayWindow
from steam_helpers import get_unturned_path
from log_reader import get_resolution


IMG = pth.join(pth.dirname(pth.abspath(__file__)), "img")


def img_path(img):
    # Get resolution
    x,y = get_resolution()
    p = pth.join(IMG, f'{x}x{y}', img)
    if not pth.exists(p):
        supported_resolutions = ', '.join([d for d in os.listdir(IMG)])
        print(f"Img_Path Resolver: Image {img} not found at {p}, are you using a supported resolution? Supported resolutions are: {supported_resolutions}")
        raise FileNotFoundError(f"Img_Path Resolver: Image {img} not found at {p}, are you using a supported resolution? Supported resolutions are: {supported_resolutions}")
    return p

def is_unturned_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() == 'unturned.exe':         
            return True
    return False

def seconds_to_hms(seconds):
    parts = []
    hours, remainder = divmod(seconds, 3600)
    if hours > 0:
        parts.append("{}h".format(int(hours)))
    minutes, seconds = divmod(remainder, 60)
    if minutes > 0:
        parts.append("{}m".format(int(minutes)))
    if seconds > 0:
        parts.append("{}s".format(int(seconds)))
    return "".join(parts)

def hms_to_seconds(hms: str) -> int:
    try:
        seconds = 0
        if 'h' in hms:
            hours, hms = hms.split('h')
            # remove any other h's
            hms = hms.replace('h', '')
            seconds += int(hours) * 3600
        if 'm' in hms:
            minutes, hms = hms.split('m')
            # remove any other m's
            hms = hms.replace('m', '')
            seconds += int(minutes) * 60
        if 's' in hms:
            # remove any other s's
            seconds += int(hms.split('s')[0].replace('s', ''))
        return seconds
    except Exception as e:
        print(f"hms_to_seconds: error: {e}")
        return 0

def kill_unturned():
    print('Helpers is killing unturned')
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == 'unturned.exe':
            p = psutil.Process(proc.info['pid'])
            p.terminate()
    
    while is_unturned_running():
        time.sleep(0.1)

def get_unturned_window() -> int:
    unturned_exe = pth.join(get_unturned_path(), "Unturned.exe")
    unturned_window_title = "Unturned"

    def callback(hwnd, hwnds):
        _, pid = GetWindowThreadProcessId(hwnd)
        try:
            process = psutil.Process(pid)
            if process.exe().lower() == unturned_exe.lower() and GetWindowText(hwnd) == unturned_window_title:
                hwnds.append(hwnd)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return True

    hwnds = []
    EnumWindows(callback, hwnds)
    if hwnds:
        return hwnds[0]

    raise Exception("Unturned window not found")

def move_mouse_delta(dx, dy):
    mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)

def turn_mouse(dx, dy, speed):
    x_steps = abs(dx) // speed
    y_steps = abs(dy) // speed

    # Move in x direction
    for _ in range(x_steps):
        move_mouse_delta(speed if dx > 0 else -speed, 0)
        time.sleep(0.01)  # sleep for 10 milliseconds

    # Move in y direction
    for _ in range(y_steps):
        move_mouse_delta(0, speed if dy > 0 else -speed)
        time.sleep(0.01)  # sleep for 10 milliseconds

def get_unturned_window_size() -> Union[int, int]:
    hwnd = get_unturned_window()
    rect = GetWindowRect(hwnd)
    return rect[2] - rect[0], rect[3] - rect[1]

def get_unturned_window_dimensions() -> Tuple[int, int, int, int]:
    hwnd = get_unturned_window()
    rect = GetWindowRect(hwnd)
    return rect[0], rect[1], rect[2], rect[3]

def focus_unturned_window():
    print("focus_unturned: finding unturned window")
    hwnd = get_unturned_window()
    # maximize window
    print(f"focus_unturned: maximizing unturned window")
    SetForegroundWindow(hwnd)
    ShowWindow(hwnd, 5)
    BringWindowToTop(hwnd)
    time.sleep(0.25)

def focus_unturned(func):
    def wrapper(*args, **kwargs):
        focus_unturned_window()
        func(*args, **kwargs)
    return wrapper

@focus_unturned
def click_image(
    image, confidence=0.8, timeout=4, x_offset=0, y_offset=0, press_key_on_fail=None,
overlay=None):
    image = img_path(image)
    print("click_image: ", image)
    s = time.time()
    while True:
        try:
            x, y = py.locateCenterOnScreen(image=img_path(image), confidence=confidence, grayscale=True, region=get_unturned_window_dimensions())
            print(f"found {image} at {x}, {y} [{int(time.time()-s/1000)}ms]")
            x += x_offset
            y += y_offset
            break
        except Exception as e:
            focus_unturned_window()
            print(f"click_image: image: {image} error: {e} [{round(time.time() - s, 2)}s/{timeout}s]")
            if time.time() - s > timeout:
                raise f"image {image} not found"
            if press_key_on_fail is not None:
                py.press(press_key_on_fail)
                # Click in the corner incase the menu button is highlighted
                size_x, size_y = get_unturned_window_size()
                # click in the top left corner (x and y size minus 10)
                py.click(size_x+10, size_y+10)
                time.sleep(0.1)
            continue
    py.leftClick(x, y)
    if isinstance(overlay, OverlayWindow):
        print('drawing dot!')
        overlay.draw_dot(x, y, duration=0.5, size=2.5)

    if x_offset != 0 or y_offset != 0:
        print(f"clicked {image} at {x}, {y} with offset {x_offset}, {y_offset}")
        return
    print(f"clicked {image} at {x}, {y}")




if __name__ == '__main__':
    while True:
        s = input("hms:")
        print(hms_to_seconds(s))