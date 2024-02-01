import os
import json
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')

class KeyPressEater(QtCore.QObject):
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            modifiers = event.modifiers()
            if modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_P:
                print("Ctrl+P pressed")
                return True
        return super().eventFilter(obj, event)

def save_setting(key, value):
    if 'webhookUrlTextBox' in key or 'password' in key.lower():
        # censor the webhook url
        # replace second half of the url with asterisks
        l = len(value)
        print(f"Saving secret setting: {key} = {value[:l//4]}{'*' * (int(l*3//4))}")

    else:
        print(f"Saving setting: {key} = {value}")
    with open(SETTINGS_FILE, 'r') as f:
        settings = json.load(f)
    settings[key] = value
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def load_setting(key):
    # Create the settings file if it doesn't exist
    if not os.path.exists(SETTINGS_FILE):
        print("Creating settings file")
        with open(SETTINGS_FILE, 'w') as f:
            json.dump({}, f, indent=4)
    # Load the settings file
    with open(SETTINGS_FILE, 'r') as f:
        settings = json.load(f)
        if 'webhookUrlTextBox' in key or 'password' in key.lower():
            # censor the webhook urlI
            # replace second half of the url with asterisks
            l = len(settings.get(key, ''))
            print(f"Loading secret setting: {key} = {settings.get(key, '')[:l//4]}{'*' * (int(l*3//4))}")
            # print(f"Loading setting: {key} = {settings.get(key, '')}")
            
        else:
            print(f"Loading setting: {key} = {settings.get(key, None)}")
    return settings.get(key, None)


def init(widget: QtWidgets.QWidget):
    """
    Load the settings from the settings.json file and apply them to the widgets
    Assigns the save_setting function to the widgets respective signals
    """
    val = load_setting(widget.objectName())

    # Checkbox
    if isinstance(widget, QtWidgets.QCheckBox):
        # Default to current value if the setting doesn't exist
        if val is None:
            val = widget.isChecked()
        widget.setChecked(val)
        widget.stateChanged.connect(lambda: save_setting(widget.objectName(), widget.isChecked()))

    
    # LineEdit
    elif isinstance(widget, QtWidgets.QLineEdit):
        if val is None:
            val = widget.text()

        widget.setText(val)
        widget.textChanged.connect(lambda: save_setting(widget.objectName(), widget.text()))

        print(f"save_widgets.init: Setting up shortcut for {widget.objectName()}")
        eater = KeyPressEater()
        widget.installEventFilter(eater)

    # Slider
    elif isinstance(widget, QtWidgets.QSlider):
        if val is None:
            val = widget.value()

        widget.setValue(val)
        widget.sliderReleased.connect(lambda: save_setting(widget.objectName(), widget.value()))
    
    # ComboBox
    elif isinstance(widget, QtWidgets.QComboBox):
        if val is None:
            val = widget.currentText()

        print("Setting combobox to", val)
        widget.setCurrentText(val)
        widget.currentIndexChanged.connect(lambda: save_setting(widget.objectName(), widget.currentText()))
    
    # SpinBox
    elif isinstance(widget, QtWidgets.QSpinBox):
        if val is None:
            val = widget.value()

        widget.setValue(val)
        widget.valueChanged.connect(lambda: save_setting(widget.objectName(), widget.value()))
    
    # Checkable group box
    elif isinstance(widget, QtWidgets.QGroupBox):
        if val is None:
            val = widget.isChecked()

        widget.setChecked(val)
        widget.toggled.connect(lambda: save_setting(widget.objectName(), widget.isChecked()))

    else:
        raise Exception(f"Widget type {type(widget)} not supported for saving/loading settings")