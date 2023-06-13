import os
import glob
import binascii
import random
import string
import datetime
import time


def func_rename(location, pattern, newName):
    for file in glob.iglob(os.path.join(location, pattern)):
        filename, extension = os.path.splitext(os.path.basename(file))
        os.rename(file, os.path.join(location, newName % filename + extension))
# 1st argument is the path
# 2nd argument is file pattern
# 3rd argument is the new filename, e.g. 'new %s'
# func_rename('C:\\Users\\Admin\\sheet\\','*.*','old %s')


def func_file_to_hex(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    with open(output_file, 'w') as f:
        f.write(binascii.hexlify(content).decode('utf-8'))


def func_hex_to_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    with open(output_file, 'w') as f:
        f.write(binascii.unhexlify(content).decode('utf-8'))
# func_file_to_hex('C:\\Users\\Admin\\listOfCommands.txt','C:\\Users\\Admin\\listOfCommands.hex')
# func_hex_to_file('C:\\Users\\Admin\\listOfCommands.hex','C:\\Users\\Admin\\listOfCommands1.txt')


def func_password_generator(length):
    character_pool = string.ascii_letters + string.digits + string.punctuation
    output = ''.join(random.choice(character_pool) for i in range(length))
    return output
# print(func_password_generator(16))


def func_vowel_checker(word):
    vowels = "aeiouAEIOU"
    output = word
    moved_chars = ''
    for character in word:
        if character not in vowels:
            moved_chars += character
            output = output[1:]
        else:
            break
    return (output + moved_chars + "ay ")


def func_english_to_piglatin(sentence):
    vowels = "aeiouAEIOU"
    output = ""
    print("original : " + sentence)
    for word in sentence.split():
        if word[0] in vowels:
            output += word + "yay "
        else:
            output += func_vowel_checker(word)
    return output
# print(func_english_to_piglatin("Hell you have a nice house"))


def func_piglatin_to_english(sentence):
    output = ""
    print("pig latin : " + sentence)
    for word in sentence.split():
        if word[-3:] == 'yay':
            output += word[:-3] + " "
        else:
            output += word[-3:-2] + word[:-3] + " "
    return output
# print(func_piglatin_to_english("ellHay ouyay avehay ayay icenay ousehay"))


def func_calculate_pi_digits(digits):
    for i in range(digits):
        return 22/7


def pomodoro_timer(numberOfReps):
    print("\t##POMODORO TIMER##")
    print("25 minutes of work followed by")
    print("5 minutes of break")
    work_remaining = 25 * 60
    rest_remaining = 5 * 60

    print("Number of Pomodoros remaining: " + str(numberOfReps))
    while numberOfReps > 0:
        print("Time remaining until next REST")
        while work_remaining > 0:
            timer = datetime.timedelta(seconds=work_remaining)
            print(timer, end="\r")
            time.sleep(1)
            work_remaining -= 1
        print("Work time finished. Please rest now!")
        print("Time remaining until next WORK")
        while rest_remaining > 0:
            timer = datetime.timedelta(seconds=rest_remaining)
            print(timer, end="\r")
            time.sleep(1)
            rest_remaining -= 1
        print("Rest time finished. Back to work!")
        numberOfReps -= 1
        pomodoro_timer(numberOfReps)

    print("All pomodoros completed. Please take a longer rest and come back\n")
    time.sleep(5)


# pomodoro_timer(4)

def apply_rot13(message):
    mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                            'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return message.translate(mapping)


# pass the message. Same function can be called for both encryption and decryption
# print(apply_rot13("Uryyb NOPnop"))

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


# heads_or_tails()
