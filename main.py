import binascii
import random
import string


def func_password_generator(length):
    character_pool = string.ascii_letters + string.digits + string.punctuation
    output = ''.join(random.choice(character_pool) for i in range(length))
    return output
# print(func_password_generator(16))


def func_calculate_pi_digits(digits):
    for i in range(digits):
        return 22/7
