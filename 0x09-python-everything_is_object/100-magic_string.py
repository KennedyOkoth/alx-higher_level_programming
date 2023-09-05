#!/usr/bin/python3
<<<<<<< HEAD
def magic_string():
    magic_string.counter = getattr(magic_string, "counter", 0) + 1
    return ", ".join(["BestSchool" for i in range(magic_string.counter)])
=======
def magic_string(my_list=[]):
    magic_string.append("BestSchool")
    return ", ".join(my_list)
>>>>>>> 363a44644cf592c83fd0a39fd4cba0c12a9b5d0f
