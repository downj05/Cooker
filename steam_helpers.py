from registry_helpers import *
import os
import vdf

UNTURNED_APP_ID = 304930

def get_steam_path():
    key_path = "SOFTWARE\Valve\Steam"
    value_name = "SteamPath"
    return get_registry_value(key_path, value_name)

def get_steam_drive():
    return get_steam_path().split(":")[0].upper()

DRIVE_LETTER = get_steam_drive()

STEAM_EXECUTABLE = os.path.join(get_steam_path(), "steam.exe")



def get_steam_logins_by_modified():
    # Get the steamid3's of all the previously logged in Steam users on this machine
    # Sorts them by modification date
    dir_path = rf'{DRIVE_LETTER}:\Program Files (x86)\Steam\userdata' 
    files = os.listdir(dir_path)
    files_with_mtime = [(f, os.stat(os.path.join(dir_path, f)).st_mtime) for f in files]
    sorted_files = sorted(files_with_mtime, key=lambda x: x[1])
    return sorted_files

def steamid3_to_steam64(steamid3):
	universe = 1  # The default universe for most Steam accounts
	account_id = int(steamid3.split(":")[2])  # Extract the account ID from the SteamID3 string
	steam64 = (account_id + 76561197960265728) | (universe << 56)  # Construct the 64-bit SteamID
	return steam64


def get_steam_current_id3_from_registry():
    # Open the registry key for reading
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Valve\Steam\ActiveProcess')

    # Read the ActiveUser value as a REG_DWORD
    active_user, _ = winreg.QueryValueEx(key, 'ActiveUser')

    # Convert the value to a base-10 integer
    active_user_int = int(active_user)

    # Close the registry key
    winreg.CloseKey(key)

    # Print the value as an integer
    return active_user_int

def select_all_steam64():
    steamid3_list = get_steam_logins_by_modified()
    steamid64_list = []
    for s, modified in steamid3_list:
        steamid64_list.append(steamid3_to_steam64(f"U:1:{s}"))
    return steamid64_list

def get_latest_user_steam64():
    # Get the steam64 of the latest user logged into Steam on the users machine
    # Pull active user from registry
    steamid3 = get_steam_current_id3_from_registry()
    steam64 = steamid3_to_steam64(f"U:1:{steamid3}")
    return steam64

class ClientIDList:
    @staticmethod
    def ids() -> list[int]:
        """
        Get all of the steam64 ids of the users logged into Steam on the users machine
        :returns: list of steam64 ids
        """
        return select_all_steam64()

    @staticmethod
    def latest() -> int:
        """
        Get the steam64 of the latest user logged into Steam on the users machine
        :returns: latest users steam64 id
        """
        return get_latest_user_steam64()


def get_steam_library():
    """
    Returns a VDF dictionary of all of the Steam libraries on the users machine, spanning multiple drives
    It also shows where the Steam games are installed, and to which library they belong.
    """
    vdf_path = os.path.join(get_steam_path(), "steamapps", "libraryfolders.vdf")
    with open(vdf_path, 'r') as f:
        libraries = vdf.loads(f.read(), mapper=vdf.VDFDict)['libraryfolders']
    return libraries

def get_unturned_drive():
    libraries = get_steam_library()
    for key,value in libraries.items():
        path = value['path']
        for app in value['apps']:
            if app == str(UNTURNED_APP_ID):
                return path.split(":")[0].upper()
    print("Error: Unturned not found in Steam libraries")
    return None



def get_unturned_path():
    libraries = get_steam_library()
    for library in libraries.values():
        if 'apps' in library and str(UNTURNED_APP_ID) in library['apps']:
            return os.path.join(library['path'], 'steamapps', 'common', 'Unturned')
    return None

UNTURNED_EXECUTABLE = os.path.join(get_unturned_path(), "Unturned.exe")
UNTURNED_BE_EXECUTABLE = os.path.join(get_unturned_path(), "Unturned_BE.exe")


import subprocess

def launch_steam_game(id: int):
    DEFAULT_ARGS = "-width 640 -height 480 -FrameRateLimit 20 -fullscreenmode 3 -ui_scale 1.0"
    subprocess.Popen(f'"{STEAM_EXECUTABLE}" -applaunch {id} {DEFAULT_ARGS}', shell=True)
    print(f"launch_steam_game: launched game with arguments: {DEFAULT_ARGS}")

if __name__ == '__main__':
    launch_steam_game(UNTURNED_APP_ID)
