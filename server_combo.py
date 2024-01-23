from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QComboBox, QLineEdit, QPushButton
from ui_helpers import show_message, input_dialog

import json
"""
example server dict:

{
    'server1': {
        'ip': '123.456.789.012',
        'port': 27015,
        'password': 'password',
        }
}
"""

def save_server(server_dict, name, ip, port, password):
    pass


test_dict = {
    'server1': {
        'ip': '123.456.789.012',
        'port': 27015,
        'password': 'password',
    },
    'server2': {
        'ip': 'server.thing.net',
        'port': 27017,
        'password': '',
    },
}

def save_dict_to_file(server_dict):
    with open('settings.json', 'r') as f:
        db_dict = json.load(f)    
    
    db_dict['server_list'] = server_dict

    with open('settings.json', 'w') as f:
        json.dump(db_dict, f, indent=4)

def load_dict_from_file():
    with open('settings.json', 'r') as f:
        db_dict = json.load(f)

    return db_dict.get('server_list', {})

class ServerComboBoxLogic(QObject):
    def __init__(self, saveBtn: QPushButton, updateBtn: QPushButton, deleteBtn: QPushButton, serverComboBox: QComboBox, ipLineEdit: QLineEdit, portLineEdit: QLineEdit, passwordLineEdit: QLineEdit):
        super(ServerComboBoxLogic, self).__init__()
        self._servers = load_dict_from_file()
        self._serverComboBox = serverComboBox

        self._saveBtn = saveBtn
        self._updateBtn = updateBtn
        self._deleteBtn = deleteBtn

        self._ipLineEdit = ipLineEdit
        self._portLineEdit = portLineEdit
        self._passwordLineEdit = passwordLineEdit


        self._saveBtn.clicked.connect(self.save)
        self._updateBtn.clicked.connect(self.update)
        self._deleteBtn.clicked.connect(self.delete)
        self._serverComboBox.currentIndexChanged.connect(self.update_fields)

        self.update_server_combo_box()

    def update_server_combo_box(self):
        for server in self._servers:
            self._serverComboBox.addItem(server)

        # see if a server was selected and update the fields
        if self._serverComboBox.currentText():
            self.update_fields(self._serverComboBox.currentIndex())
        else:
            print("Server combox has no text:", self._serverComboBox.currentText())
    
    def delete(self):
        try:
            del self._servers[self._serverComboBox.currentText()]
            self._serverComboBox.removeItem(self._serverComboBox.currentIndex())
        except KeyError:
            show_message(self._serverComboBox, "Error", "Selected server does not exist!")
            return
        
        save_dict_to_file(self._servers)

        self._serverComboBox.setCurrentIndex(0)
        self.update_fields(0)


    def update(self):
        try:
            server = self._servers[self._serverComboBox.currentText()]
        except KeyError:
            show_message(self._serverComboBox, "Error", "Selected server does not exist!")
            return

        server['ip'] = self._ipLineEdit.text()
        server['port'] = int(self._portLineEdit.text())
        server['password'] = self._passwordLineEdit.text()

        save_dict_to_file(self._servers)

    
    def update_fields_from_server(self, server: dict):
        self._ipLineEdit.setText(server['ip'])
        self._portLineEdit.setText(str(server['port']))
        self._passwordLineEdit.setText(server['password'])

    def update_fields(self, index):
        try:
            server = self._servers[self._serverComboBox.currentText()]
        except KeyError:
            show_message(self._serverComboBox, "Error", "Selected server does not exist!")
            return

        self.update_fields_from_server(server)

    def save(self):
        name = input_dialog(self._serverComboBox, "Server Name", "Enter a name for the server")
        if name is None:
            return

        ip = self._ipLineEdit.text()
        port = self._portLineEdit.text()
        password = self._passwordLineEdit.text()


        self._servers[name] = {
            'ip': ip,
            'port': int(port),
            'password': password
        }
        self._serverComboBox.addItem(name)
        self._serverComboBox.setCurrentText(name)
        save_dict_to_file(self._servers)