def zeroMatrix(matrix):
    rows = len(matrix)
    # matrices are rectangular so measuring len of first row gives us len of all cols
    cols = len(matrix[0])
    new_rows = []
    new_cols = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                new_rows.append(row)
                new_cols.append(col)

    for row in new_rows:
        nullifyRow(matrix,row)

    for col in new_cols:
        nullifyCols(matrix,col)

    return matrix

def nullifyRow(matrix,row):
    # iterating through all columns
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCols(matrix,col):
    # iterating through all rows
    for i in range(len(matrix)):
        matrix[i][col] = 0

matrix = [[1,2,2,3],
          [2,0,0,1]]

#print(zeroMatrix(matrix))




