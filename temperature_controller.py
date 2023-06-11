import random

# recursion based temperature control

# provide target temperature as argument


def simple_temperature_control(target_temperature):
    input_temperature = random.randint(0, 35)
    print("Current temperature:\t" + str(input_temperature))
    if input_temperature < target_temperature:
        print("Target not reached. Starting heater")
        simple_temperature_control(target_temperature)
    if input_temperature > target_temperature:
        print("Target exceeded. Starting cooler")
        simple_temperature_control(target_temperature)
    if input_temperature == target_temperature:
        print("Target reached.")


simple_temperature_control(25)
