import random
from collections import Counter

def roll_dice(num_dice=5):
    return [random.randint(1, 6) for _ in range(num_dice)]

def display_dice(dice):
    print("Your dice: ", " ".join(str(die) for die in dice))

def reroll_dice(dice):
    reroll_indices = input("Enter the dice positions (1-5) you want to reroll, separated by spaces: ").split()
    for i in reroll_indices:
        dice[int(i) - 1] = random.randint(1, 6)

def calculate_score(dice):
    counts = Counter(dice)
    if 5 in counts.values():
        return "Yahtzee! Score: 50"
    elif 4 in counts.values():
        return "Four of a kind! Score: 30"
    elif 3 in counts.values() and 2 in counts.values():
        return "Full House! Score: 25"
    elif 3 in counts.values():
        return "Three of a kind! Score: 15"
    elif len(counts) == 5 and (max(dice) - min(dice) == 4):
        return "Large Straight! Score: 40"
    elif len(counts) == 4 or (len(counts) == 5 and max(dice) - min(dice) == 3):
        return "Small Straight! Score: 30"
    else:
        return f"Chance! Score: {sum(dice)}"

def play_yahtzee():
    dice = roll_dice()
    display_dice(dice)
    
    for _ in range(2):
        reroll = input("Do you want to reroll any dice? (y/n): ").lower()
        if reroll == 'y':
            reroll_dice(dice)
            display_dice(dice)
        else:
            break
    
    print(calculate_score(dice))

if __name__ == "__main__":
    play_yahtzee()
