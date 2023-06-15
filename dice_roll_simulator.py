import random


def get_random_dice_value():
    return random.randint(1, 6)


def roll_dice():
    value = get_random_dice_value()
    print(value)
    if value in [1, 6]:
        roll_dice()


no_of_dices = int(input("Number of dices to roll at once:\t"))
for i in range(no_of_dices):
    roll_dice()
