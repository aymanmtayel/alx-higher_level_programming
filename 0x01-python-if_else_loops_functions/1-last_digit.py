#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l = abs(number) % 10
if (number > 0 and l > 5):
    print(f"Last digit of {number} is {l} and is greater than 5")
elif (number > 0 and 0 < l < 6):
    print(f"Last digit of {number} is {l} and is less than 6 and not 0")
elif (number < 0 and l > 0):
    print(f"Last digit of {number} is {-1 * l} and is less than 6 and not 0")
elif (l == 0):
    print(f"Last digit of {number} is {l} and is 0")
