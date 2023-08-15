#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        int_max = 0
        for i in my_list:
            if i > int_max:
                int_max = i
    return int_max


# if __name__ == "__main__":
#     my_list = [1, 90, 2, 13, 34, 5, -13, 3]
#     max_value = max_integer(my_list)
#     print("Max: {}".format(max_value))
