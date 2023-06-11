import time
import random
# range
bottom_floor = -2
top_floor = 15

# randomize starting position


def get_random_floor():
    return random.randint(bottom_floor, top_floor)


class Elevator:
    def __init__(self, top_floor, bottom_floor, current_floor):
        self.current_floor = current_floor
        self.floor_range = range(bottom_floor, top_floor+1)

    def go_up(self):
        self.current_floor += 1

    def go_down(self):
        self.current_floor -= 1

    def is_floor_reached(self, user_choice):
        return self.current_floor == user_choice

    def is_valid_floor(self, user_choice):
        return user_choice in self.floor_range and (user_choice != self.current_floor)

    def get_current_floor(self):
        return self.current_floor


now = get_random_floor()
obj = Elevator(top_floor, bottom_floor, now)

print("You are at floor: "+str(now))
user_choice = int(input("Enter a floor number between " +
                  str(bottom_floor)+" and "+str(top_floor)+":\t"))
# input validation
if obj.is_valid_floor(user_choice):
    # get current position
    current = obj.get_current_floor()
    print("Currently at floor:\t"+str(current))
    reached = False
    while reached == False:
        if user_choice > current:
            obj.go_up()
        if user_choice < current:
            obj.go_down()
        time.sleep(1)
        print("Reached floor:\t"+str(obj.get_current_floor()))
        reached = obj.is_floor_reached(user_choice)
else:
    print("Please enter a valid floor between " +
          str(bottom_floor)+" and "+str(top_floor))
