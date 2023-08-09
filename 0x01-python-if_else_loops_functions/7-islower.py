def islower(c):
    # Check if the character is within the ASCII range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')

# Test the function
print(islower('a'))  # Should print True
print(islower('A'))  # Should print False
print(islower('1'))  # Should print False
