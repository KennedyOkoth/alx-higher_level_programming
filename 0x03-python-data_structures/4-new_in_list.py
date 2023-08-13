#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return my_list
    for i in range(len(new_list)):
        if i == idx:
            new_list[i] = element
            return new_list
    return my_list


# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     idx = 3
#     new_element = 9
#     new_list = new_in_list(my_list, idx, new_element)

#     print(new_list)
#     print(my_list)
