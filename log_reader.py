
import queue
import re
import time
import os
import steam_helpers
from PyQt5.QtCore import QThread



LOG_FILE = os.path.join(steam_helpers.get_unturned_path(), "Logs", "Client.log")
print(f"Extracting logs from: {LOG_FILE}")


# if a log line has any of these strings in it, ignore it
IGNORE_SENTENCES = ["Look rotation viewing vector is zero"]

PATTERN = r"(?:Applying graphics settings \()(.*)(?:\))"

def wait_for_pattern(pattern) -> re.Match:
    # Keep track of the last line number that was read
    last_line = 0
    while True:
        # Get the size of the log file
        size = os.path.getsize(LOG_FILE)

        # If the size of the file has decreased (e.g., due to log rotation),
        # reset the last_line variable to the beginning of the file
        if size < last_line:
            last_line = 0

        # Open the file and seek to the last line that was read
        with open(LOG_FILE, encoding="utf-8") as f:
            f.seek(last_line)

            # Read any new lines and print them
            for line in f:
                # Avoid dumping entire log contents on startup
                if last_line > 0:
                    if not any(s in line for s in IGNORE_SENTENCES):
                        m = re.search(pattern, line)
                        if m:
                            print("Match found!")
                            return m

            # Update the last_line variable to the current position
            if last_line == 0:
                pass
                # print("Logs extracted, monitoring for updates...")
            last_line = f.tell()

        # Wait for a few seconds before checking again
        time.sleep(0.1)


def get_all_lines(pattern) -> re.Match:
    # Get all lines that match the pattern
    with open(LOG_FILE, encoding="utf-8") as f:
        lines = f.readlines()
        matches = [re.search(pattern, line) for line in lines]
        # Prune out the None values
        matches = [m for m in matches if m]
        return matches

def get_resolution():
    resolution_pattern = r"(?:Requesting resolution change: (?:FullScreenWindow|Windowed|ExclusiveFullScreen) )(\d+)(?: x )(\d+)"
    last = get_all_lines(resolution_pattern)[-1]
    return int(last.group(1)), int(last.group(2))

def get_battle_eye():
    """
    Gets the last line that contains the battle eye pattern
    This should only be run after a client has started to join a server
    """
    battle_eye_pattern = r"(?:Server is BattlEye secure: )()"
    last = get_all_lines(battle_eye_pattern)[-1]
    if last.group(1) == "True":
        return True
    else:
        return False


def is_in_game():
    """
    Check if the most recent log line contains the "Joining" pattern
    or the "Leaving" pattern
    """
    last_status_pattern = r"(Disconnecting: .*|Accepted by server)"
    last = get_all_lines(last_status_pattern)
    if len(last) == 0:
        return False
    last = last[-1]
    if "Disconnecting" in last.group(1):
        return False
    elif "Accepted by server" in last.group(1):
        return True
    else:
        return False


class LogReaderThread(QThread):
    """
    A Thread that monitors the log file for a pattern match
    Uses an array to share data between threads.
    The first element is a boolean that is set to false when the pattern is found
    The second element is the match object
    """
    def __init__(self, pattern, shared_var):
        QThread.__init__(self)
        self.pattern = pattern
        self.shared_var = shared_var

    def run(self):
        while True:
            match = wait_for_pattern(self.pattern)
            self.shared_var[0] = False
            self.shared_var[1] = match
            print(f"LogReaderThread: Pattern found {match}!")

if __name__ == "__main__":
    print(f'{get_resolution()[0]} x {get_resolution()[1]}')
    print(f"Battle eye: {get_battle_eye()}")