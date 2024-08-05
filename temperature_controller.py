# recursion based temperature control
import random
import time

# global min and max values
temp_low = 16
temp_high = 32

def simple_temperature_control(target):
    from_sensor = random.randint(temp_low, temp_high)   #replace with sensor reading
    print(f"Current reading:\t{from_sensor}")
    time.sleep(1)   #wait x time before checking
    if from_sensor < target:
        print("Target not met. Increasing heater power")
        simple_temperature_control(target)
    if from_sensor > target:
        print("Target exceeded. Increasing cooler power")
        simple_temperature_control(target)
    if from_sensor == target:
        print("Target met. All components turned off")


set_temp = 26   #replace to user input
print(f"User set temperature at\t{set_temp}")
simple_temperature_control(set_temp)
