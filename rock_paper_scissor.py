import random


def rock_paper_scissor():
    print("Starting rock paper scissor game")
    user_wins = [(0, 2), (1, 0), (2, 1)]
    computer_wins = [(0, 1), (1, 2), (2, 0)]
    print("0 for rock")
    print("1 for paper")
    print("2 for scissor")

    user_choice = int(input("make a selection (0,1,2)\t"))
    computer_choice = random.randint(0, 2)
    print("Computer selected\t" + str(computer_choice))
    outcome_pair = (user_choice, computer_choice)
    if (user_choice == computer_choice):
        print("It's a draw. Try AGAIN!")
        rock_paper_scissor()
    if (outcome_pair in user_wins):
        print("Winner: YOU")
    if (outcome_pair in computer_wins):
        print("Winner: Computer")


rock_paper_scissor()
