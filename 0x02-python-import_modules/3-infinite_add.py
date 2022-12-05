#!/usr/bin/python3

import sys

# Check if there are any command-line arguments
if len(sys.argv) > 1:
  # Initialize the result variable
  result = 0

  # Loop through the command-line arguments
  for i in range(1, len(sys.argv)):
    # Add the current argument to the result
    result += int(sys.argv[i])

  # Print the result
  print(result)

