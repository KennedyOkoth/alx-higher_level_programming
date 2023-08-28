#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function

    Args:
        my_list (list, optional): A list containing any type of integers.
        x (int, optional):  represents the number of elements to access in my_list.
        x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur

    Returns:
        _type_: integer elements
    """
    try:
        count = 0
        for i in my_list:
            try:
                i = int(i)
            except:
                continue
            print("{:d}".format(i), end="")
            count += 1
            if count >= x:
                break
        print()
        return count
    except:
        return count


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
