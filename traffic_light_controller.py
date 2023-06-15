import time
import datetime


class TrafficLight:
    LIGHT_CHOICES = ['RED', 'YELLOW', 'GREEN']

    def __init__(self, duration):
        self.duration = duration
        self.current = 'RED'

    def display_board(self):
        print(self.LIGHT_CHOICES)
    # establishes a timer for each current light and display until timer expires

    def work_current(self):
        print("Current display", self.current)
        remaining = self.duration
        while remaining >= 0:
            timer = datetime.timedelta(seconds=remaining)
            print(timer, end="\r")
            time.sleep(1)
            remaining -= 1
        print("\n")
    # switch between light. This function could be more elegant

    def get_next(self, current):
        if current == 'RED':
            return 'YELLOW'
        if current == 'YELLOW':
            return 'GREEN'
        if current == 'GREEN':
            return 'RED'

    def change_current(self):
        self.current = self.get_next(self.current)

    def start(self):
        while True:
            self.work_current()
            self.change_current()


# pass light duration
obj = TrafficLight(5)
# display board
obj.display_board()
# start infinite light cycle
obj.start()
