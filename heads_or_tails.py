import random


def heads_or_tails():
    print("starting heads or tails game")
    print("Type heads or tails")
    user_choice = input("--")
    possible_combo = ["HEADS", "TAILS"]
    results = random.choice(possible_combo)
    print(results)
    if (user_choice.upper() == results):
        print("You won!")
    else:
        print("You lost")


heads_or_tails()
