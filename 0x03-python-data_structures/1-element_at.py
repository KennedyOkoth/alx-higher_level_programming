#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for x in range(len(my_list)):
        if x == idx:
            return my_list[x]
    return None


# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5, 8, 7, 4, 5, 3, 2]
#     idx = 6
#     print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
