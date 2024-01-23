from PyQt5.QtCore import QThread, pyqtSignal, QObject, QEventLoop
from PyQt5.QtWidgets import QPushButton
from gui import Ui_MainWindow
import game_functions as game
import time
import helpers
import traceback
import webhook
from ui_helpers import show_message
from log_reader import LogReaderThread

class StartCookerButtonLogic(QObject):
    def __init__(self, button: QPushButton, window: Ui_MainWindow):
        super().__init__()
        print(f"StartCookerButtonLogic: init, {window.serverIP.text()}")
        self.window = window
        self.button = button
        print(f"StartCookerButtonLogic: connect StartCookerButtonLogic.startCookerEvent to button.clicked")
        self.button.clicked.connect(self.startCookerEvent)

    def startCookerEvent(self):
            print("StartCookerButtonLogic: startCookerEvent fired")
            ip = self.window.serverIP.text()
            port = self.window.serverPort.text()
            password = self.window.serverPassword.text()


            try:
                # self.overlay = OverlayWindow()
                # self.overlay.show()
                # dim = self.overlay.geometry()
                # self.overlay.play_gif("oven.gif", dim.width() / 2 - 100, dim.height() / 2 - 100, 200, 200, duration=1)
                # If unturned isnt open, open it via GUI
                # if not game.is_unturned_running():
                #     self.startGame.click()
                print("StartCookerButtonLogic: starting cooker loop")
                self.cookerLoop(ip, port, password)

            except Exception as e:
                print('GUI failed to join server')
                traceback.print_exc()
                show_message(self.window.startCooker, "Error", f"Failed to join server\n{e}")
                return



    def cookerLoop(self, ip, port, password):

        def loopJoinServer():
            # Join server using button
            print("cookerLoop: Joining server")
            s = time.time()
            self.window.joinServerButton.click()
            print("cookerLoop: Waiting for joined_server to be true")
            while self.window.joined_server == False:
                print("cookerLoop: Waiting for joined_server to be true")
                time.sleep(5)
            print(f"cookerLoop: Join server took {time.time() - s} seconds or {time.time() - START_TIME}")

        # Start time is the time the script started, it doesnt change
        # total time on server is the total time actually spent on the server (not including disconnects, time in menus, etc)
        START_TIME, total_time = time.time(), 0
        time_in_game = 0
        
        rejoins_session = 0

        # Webhook init
        if self.window.webhookEnabledCheckBox.isChecked():
            w = webhook.Webhook(self.window.webhookUrlTextBox.text())
        else:
            w = None

        loopJoinServer()
        
        # Announce server join
        if w is not None:
            print("cookerLoop: Sending status webhook")
            # New call
            status_tuple = (time_in_game, total_time, self.window.cookTimeSlider.value())
            w.info(status_tuple=status_tuple, rejoins_session=rejoins_session)

        
        # First element is a boolean that is set to false when the pattern is found
        # Second element is the match object that is set when the pattern is found
        connected_to_server = [True, None]

        # Create seperate log reader thread to monitor for disconnects
        print("cookerLoop: Creating log reader thread")
        thread = LogReaderThread(r"(?:Disconnecting: )(.*)", connected_to_server)
        thread.start()


        print("cookerLoop: Starting cooker loop")
        while True:
            print("cookerLoop: Starting cooker loop iteration")
            # Take time at start of loop to calculate session time + total time
            s = time.time()
            # 'Wiggle' logic
            game.frank_b_oogie(loop=False)


            # Disconnect + Rejoin logic
            if connected_to_server[0] == False:
                print("Disconnected from server!")
                reason = connected_to_server[1].group(1)
                print("Reason: ", reason)

                # Ban logic
                if "ban" in reason.lower():
                    # Error
                    if w is not None:
                        w.error((time_in_game, total_time, self.window.cookTimeSlider.value()))
                    # Focus GUI
                    self.window.activateWindow()
                    self.window.raise_()
                    show_message(self.window.startCooker, "BAN ALERT DURING COOKING!", f"Disconnected from server\nReason: {reason}")
                    print(f"BAN ALERT DURING COOKING! {reason}")



                    return
                else: # Kick logic
                    print("User was kicked/exited from the server!")
                    # Send warning
                    if w is not None:
                        w.warning(reason=reason, status_tuple=(time_in_game, total_time, self.window.cookTimeSlider.value()))

                    # Rejoin logic
                    print("Attempting to reconnect...")
                    loopJoinServer()
                    # Set connected to server to true
                    connected_to_server[0] = True
                    connected_to_server[1] = None
                    print("Reconnected to server!")

                    # Announce server join
                    if w is not None:
                        w.info(status_tuple=(time_in_game, total_time, self.window.cookTimeSlider.value()), rejoins_session=rejoins_session, message="Rejoined server")

                    rejoins_session += 1
            else:

                # Check if user can send a periodic webhook
                if self.window.webhookPostPeriodicCheckBox.isChecked():
                    # Use self.webhookPeriodicIntervalSlider.value() as the interval
                    # Compare with total_time elapsed using modulo
                    if int(total_time) % int(self.window.webhookPeriodicIntervalSlider.value()) == 0:
                        print(f"posting periodic webhookint {int(total_time) % int(self.window.webhookPeriodicIntervalSlider.value())}")
                        if w is not None:
                            w.info(status_tuple=(time_in_game, total_time, self.window.cookTimeSlider.value()), rejoins_session=rejoins_session, message="Periodic update!")
                    else:
                        print(f"not posting periodic webhookint {int(total_time) % int(self.window.webhookPeriodicIntervalSlider.value())}")

               

                # Update time in game
                time_in_game += time.time() - s

            # Update total time on server
            total_time += time.time() - s

            # Check if user has cooked for long enough
            if total_time > self.window.cookTimeSlider.value():
                break

            print(f"Total time: {helpers.seconds_to_hms(total_time)} In game time: {helpers.seconds_to_hms(time_in_game)} In Game: {connected_to_server[0]}")


        print("Cooking complete!")
        if w is not None:
            w.success(status_tuple=(time_in_game, total_time, self.window.cookTimeSlider.value()))
        game.kill_unturned()
        show_message(self.window.startCooker, "Cooking complete!", f"Cooking complete!\In-game time: {helpers.seconds_to_hms(time_in_game)}\nTotal time: {helpers.seconds_to_hms(total_time)}")
        return