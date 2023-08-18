#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set((my_list))
    new_list = list((new_set))
    result = sum(new_list)
    return result


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
