#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        value = ord(str[i])
        if value > 96 and value < 123:
            value -= 32
        print("{}".format(chr(value)), end="")
    print()
