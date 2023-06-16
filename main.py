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


def func_calculate_pi_digits(digits):
    for i in range(digits):
        return 22/7
