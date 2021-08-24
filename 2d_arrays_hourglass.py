if __name__ == '__main__':
  matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
  for row in range(len(matrix)):
    hourglass = [matrix[row][0:3], matrix[1][1], matrix[2][0:3]]

  print(hourglass)