"""
Write an algorithm such that if an element in a MxN matrix is 0, its entire row
and columns are set to 0.
"""


def zero_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                set_none(matrix, row, column)

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] is None:
                matrix[row][column] = 0
    return matrix


def set_none(matrix, row, column):
    # Set the row to None.
    for i in range(len(matrix[row])):
        if matrix[row][i] != 0:
            matrix[row][i] = None

    # Set the column to None.
    for j in range(len(matrix)):
        if matrix[j][column] != 0:
            matrix[j][column] = None

    matrix[row][column] = None


matrix = [
  [0, 2, 3],
  [4, 5, 6],
  [7, 0, 9]
]


print(zero_matrix(matrix))
