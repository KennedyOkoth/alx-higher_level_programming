#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    length_of_argv = len(argv)
    for c in range(1, length_of_argv):
        num = int(argv[c])
        sum += num
    print(sum)
