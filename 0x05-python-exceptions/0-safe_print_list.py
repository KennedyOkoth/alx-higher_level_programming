#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                print(i, end="")
                count += 1
            else:
                break
        print()
        return count
    except TypeError:
        return count


if __name__ == "__main__":
    my_list = [1, 2, 3, "home", "y", True, 4, 5]
    safe_print_list(my_list, 2)
