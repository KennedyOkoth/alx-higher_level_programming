#!/usr/bin/python3
from sys import argv
from sys import exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    length_of_argv = len(argv) - 1
    if length_of_argv < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    num1 = int(argv[1])
    num2 = int(argv[3])
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
