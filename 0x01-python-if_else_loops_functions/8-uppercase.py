#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Convert lowercase characters to uppercase using ASCII values
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print a newline at the end

# Test the function
uppercase("Hello, World!")  # Should print "HELLO, WORLD!"
