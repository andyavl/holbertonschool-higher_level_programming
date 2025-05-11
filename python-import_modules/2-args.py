#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    print("{} argument{}".format(length, "s" if length != 1 else ""), end="")
    print("." if length == 0 else ":")

    for arg in range(length):
        print("{}: {}".format(arg + 1, argv[arg + 1]))
