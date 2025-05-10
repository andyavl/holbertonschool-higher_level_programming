#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastdigit = -number % 10 * -1
else:
    lastdigit = number % 10

if lastdigit > 5:
    phrase = "greater than 5"
elif lastdigit == 0:
    phrase = "0"
else:
    phrase = "less than 6 and not 0"

print(f"Last digit of {number} is {lastdigit} and is {phrase}")
