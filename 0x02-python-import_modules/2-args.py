#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length_of_args = len(argv) - 1
    if length_of_args == 0:
        print(f"{length_of_args} arguments.")
    elif length_of_args == 1:
        print(f"{length_of_args} argument:")
    else:
        print(f"{length_of_args} arguments:")

    for i in range(1, length_of_args + 1):
        print("{:d}: {:s}".format(i, argv[i]))
