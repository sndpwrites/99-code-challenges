import time
import random
bottom_floor = -2
top_floor = 15


def get_random_floor():
    return random.randint(bottom_floor, top_floor)


def elevator_controller(current_floor):
    number_of_floors = range(bottom_floor, top_floor)
    print("You are at floor: "+str(number_of_floors))
    user_choice = int(input("Enter a floor number(-2,10)\t"))
    if user_choice not in number_of_floors:
        print("Please enter floor within range!")
        return

    for i in number_of_floors:
        print("Currently at floor:\t"+str(i))
        time.sleep(1)
        if (i == user_choice):
            print("You have arrived at your floor")
            break


# print(get_random_floor())
elevator_controller(current_floor=get_random_floor())
