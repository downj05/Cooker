from PyQt5 import QtWidgets

def show_message(parent, title, message):
    msg = QtWidgets.QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec_()

def input_dialog(parent, title, message):
    text, ok = QtWidgets.QInputDialog.getText(parent, title, message)
    if ok:
        return text
    else:
        return None