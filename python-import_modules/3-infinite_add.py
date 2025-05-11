#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    add = 0
    for arg in range(length):
        add += int(argv[arg + 1])
    print("{}".format(add))
