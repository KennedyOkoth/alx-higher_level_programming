#!/usr/bin/python3

from sys import argv

# Print the number of arguments
print(f"Number of argument(s): {len(argv) - 1}")

# Print the arguments
if len(argv) > 1:
    print("Argument(s):")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
else:
    print(".")

