import time
import threading
import datetime
import random

class InGameWatcher(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        while True:
            print(f"Waiting for user to leave game {self.name}")
            time.sleep(random.randint(5,15))
            self.event.set()
            print(f"User left game! {self.name}")
            time.sleep(random.randint(2,5))
            print("User rejoined!")
            self.event.clear()

def seconds_to_str(s:int):
    td = datetime.timedelta(seconds=s)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h{minutes}m{seconds}s"



if __name__ == "__main__":
    in_game_event = threading.Event()
    t1 = InGameWatcher("Thread-1", in_game_event)
    t1.start()
    total_time = 0
    in_game_time = 0
    while True:
        s = time.time()
        time.sleep(2)


        # final time calculation
        if in_game_event.is_set():
            print("User left game")
            
        else:
            print("User still in game")
            in_game_time += time.time() - s
        total_time += time.time() - s
        
        print(f"Total time: {seconds_to_str(total_time)} In game time: {seconds_to_str(in_game_time)}")