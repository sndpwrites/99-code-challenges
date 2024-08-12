import random
import csv
import csv
import datetime
class Dice:
    def roll(self):
        return random.randint(1, 6)


no_of_dices = int(input("How many rolls?:\t"))
dice = Dice()
# Open the CSV file in write mode
with open('dice_rolls.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Timestamp', 'Roll #', 'Dice Roll Value'])
    # Generate and write the dice rolls to the CSV file
    for i in range(no_of_dices):
        timestamp = datetime.datetime.now()
        roll_number = i + 1
        dice_roll = dice.roll()
        writer.writerow([timestamp, roll_number, dice_roll])
        print(f"Roll#{roll_number}\t{dice_roll}")
