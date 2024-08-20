import random

def calculate_bowling_score(rolls):
    score = 0
    roll_index = 0

    for frame in range(10):
        if is_strike(rolls, roll_index):  # Strike
            score += 10 + strike_bonus(rolls, roll_index)
            roll_index += 1
        elif is_spare(rolls, roll_index):  # Spare
            score += 10 + spare_bonus(rolls, roll_index)
            roll_index += 2
        else:  # Open frame
            score += sum_of_balls_in_frame(rolls, roll_index)
            roll_index += 2

    return score

def is_strike(rolls, roll_index):
    return rolls[roll_index] == 10

def is_spare(rolls, roll_index):
    return rolls[roll_index] + rolls[roll_index + 1] == 10

def strike_bonus(rolls, roll_index):
    return rolls[roll_index + 1] + rolls[roll_index + 2]

def spare_bonus(rolls, roll_index):
    return rolls[roll_index + 2]

def sum_of_balls_in_frame(rolls, roll_index):
    return rolls[roll_index] + rolls[roll_index + 1]

def generate_random_rolls():
    rolls = []
    for frame in range(10):
        first_roll = random.randint(0, 10)
        rolls.append(first_roll)
        if first_roll == 10:  # Strike
            continue
        second_roll = random.randint(0, 10 - first_roll)
        rolls.append(second_roll)
    # Handle the extra rolls in the 10th frame if needed
    if is_strike(rolls, -2) or is_spare(rolls, -2):
        rolls.append(random.randint(0, 10))
    return rolls
# Example usage:
rolls = generate_random_rolls()
print("Total score:", calculate_bowling_score(rolls))