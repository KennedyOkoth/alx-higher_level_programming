#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_character = None
    else:
        first_character = sentence[0]
        new_tuple = tuple((length, first_character))
    return new_tuple


# if __name__ == "__main__":
#     sentence = "At school, I learnt C!"
#     length, first = multiple_returns(sentence)
#     print("Length: {:d} - First character: {}".format(length, first))
