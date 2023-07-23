"""
Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)

Matrix = array of n length whose elements are n length arrays of integers.

3x3 example:

sum_diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7
"""
#Solution

def sum_diagonals(matrix):
    x = 0
    y = list(range(0, len(matrix)))
    for i, j in list(zip(y, y[::-1])):
        x += matrix[i][i] + matrix [j][i]
    return x