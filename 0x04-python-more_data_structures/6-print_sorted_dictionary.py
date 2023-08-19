#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_keys = list(a_dictionary.keys())
    my_keys.sort()
    sorted_dict = {i: a_dictionary[i] for i in my_keys}
    return sorted_dict


if __name__ == "__main__":
    a_dictionary = {
        "language": "C",
        "Number": 89,
        "track": "Low level",
        "ids": [1, 2, 3],
    }
    print(print_sorted_dictionary(a_dictionary))
