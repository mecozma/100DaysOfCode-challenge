"""
Given a image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
"""

def rotate_matrix(matrix):
  new_matrix = []
  for row in range(0, len(matrix)):
    temp_row = []
    for col in reversed(range(0, len(matrix))):
      temp_row.append(matrix[col][row])
    new_matrix.append(temp_row)
  return matrix, new_matrix


a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
  ]


print(rotate_matrix(a))
