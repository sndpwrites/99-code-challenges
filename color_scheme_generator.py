import random

def get_random():
    return random.randint(0, 256)

def rgb_to_hex(red, green, blue):
    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)

def generate_color_scheme(color_hex):
    return f"https://www.color-hex.com/color/{color_hex.removeprefix('#')}"

new_color = generate_color_scheme(rgb_to_hex(get_random(), get_random(), get_random()))
print(new_color)