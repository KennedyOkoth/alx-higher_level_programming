def islower(c):
    # Check if the character is within the ASCII range of lowercase letters
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

