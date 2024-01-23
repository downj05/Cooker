import winreg

def set_registry_value(key_path, value_name, value):
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(key)
        print(f"Successfully set {value_name} to {value}")
    except Exception as e:
        print(f"Error setting {value_name}: {str(e)}")

def get_registry_value(key_path, value_name):
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
        value, _ = winreg.QueryValueEx(key, value_name)
        winreg.CloseKey(key)
        return value
    except Exception as e:
        print(f"Error reading {value_name}: {str(e)}")
        return None