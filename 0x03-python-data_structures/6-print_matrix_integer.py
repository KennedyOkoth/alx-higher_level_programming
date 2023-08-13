#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if k != 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][k]), end="")
        print()


# if __name__ == "__main__":
#     matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#     print_matrix_integer(matrix)
#     print("--")
#     print_matrix_integer()
