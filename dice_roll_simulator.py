import random

class Dice:
    def roll(self):
        return random.randint(1, 7)


no_of_dices = int(input("How many rolls?:\t"))
dice = Dice()
for i in range(no_of_dices):
    print(f"Roll#{i+1}\t{dice.roll()}")
