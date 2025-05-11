#!/usr/bin/python3
for number in range(0, 100):
    if number < 99:
        print("{}{}".format(int(number / 10), number % 10), end=", ")
print("{}{}".format(int(number / 10), number % 10))
