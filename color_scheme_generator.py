import random


def get_random_value():
    return random.randint(0, 255)


def rgb_to_hex(red, green, blue):
    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)


red = get_random_value()
green = get_random_value()
blue = get_random_value()

color_hex = rgb_to_hex(red, green, blue)
print("https://www.color-hex.com/color/"+str(color_hex).removeprefix('#'))
