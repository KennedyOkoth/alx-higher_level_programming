#!/usr/bin/python3

# Import the required functions from the file calculator_1.py
from calculator_1 import add, sub, mul, div

# Define the variables a and b
a = 10
b = 5

# Print the result of calling the imported functions with a and b as arguments
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))

