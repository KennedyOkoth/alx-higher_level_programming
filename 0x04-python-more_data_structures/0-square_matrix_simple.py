#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i**2 for i in row] for row in matrix]


# if __name__ == "__main__":
#     matrix = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#  ]
#     print(square_matrix_simple(matrix))
