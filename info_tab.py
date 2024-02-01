from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QLineEdit
from steam_helpers import get_latest_user_steam64, get_persona_name
import psutil
import socket
import time


class SystemInfoThread(QThread):
    update_cpu_ram = pyqtSignal(str, str)

    def __init__(self, cpu_label, ram_label, hostname_label, steam64_label, username_label):
        print("SystemInfoThread: init")
        super().__init__()
        self.cpu_label = cpu_label
        self.ram_label = ram_label
        self.hostname_label = hostname_label
        self.steam64_label = steam64_label
        self.username_label = username_label

    def run(self):
        print("SystemInfoThread: run")
        # Set hostname label to device's hostname
        self.hostname_label.setText(socket.gethostname())
        steam64 = get_latest_user_steam64()
        self.steam64_label.setText(str(steam64))
        self.username_label.setText(get_persona_name(steam64))

        while True:
            # Get CPU and RAM usage
            cpu_usage = psutil.cpu_percent()
            ram_usage = psutil.virtual_memory().percent

            # Emit signal to update CPU and RAM labels
            self.update_cpu_ram.emit(f"{cpu_usage}%", f"{ram_usage}%")

            # Wait for 1 second
            time.sleep(1)


def init_info_tab(cpu_label: QLineEdit, ram_label: QLineEdit, hostname_label: QLineEdit, steam64_label: QLineEdit, username_label: QLineEdit):
    def update_cpu_ram_labels(cpu_usage: str, ram_usage: str):
        cpu_label.setText(cpu_usage)
        ram_label.setText(ram_usage)
    system_info_thread = SystemInfoThread(cpu_label, ram_label, hostname_label, steam64_label, username_label)
    system_info_thread.update_cpu_ram.connect(update_cpu_ram_labels)
    system_info_thread.start()
    return system_info_thread