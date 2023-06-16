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


def apply_rot13(message):
    mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                            'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return message.translate(mapping)


# pass the message. Same function can be called for both encryption and decryption
# print(apply_rot13("Uryyb NOPnop"))
