import time


class TrafficLight:
    def __init__(self, duration):
        self.duration = duration
        self.current = 'RED'

    def display_board(self):
        return ['RED', 'YELLOW', 'GREEN']

    def get_current(self):
        print(self.current, end='\r')

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
        print("Currently showing:\t")
        while True:
            self.get_current()
            time.sleep(self.duration)
            self.change_current()


obj = TrafficLight(3)
print(obj.display_board())
obj.start()
