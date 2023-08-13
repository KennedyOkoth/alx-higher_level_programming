#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    for y in range(len(my_list)):
        if y == idx:
            my_list[y] = element
            return my_list
    return my_list
