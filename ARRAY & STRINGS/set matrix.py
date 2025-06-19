def sett(matrix):
    r=len(matrix)
    c=len(matrix)

    row=False
    col=False

    for i in range(r):
        if matrix[i][0]==0:
            col=True
    for j in range(c):
        if matrix[0][j]==0:
            row=True
    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0

    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if row:
        for j in range(c):
            matrix[0][j]=0

    if col:
        for i in range(r):
            matrix[i][j]=0

    return matrix


matrix = [
 [1, 0, 3],
 [4, 5, 6],
 [7, 8, 9]
]
print(sett(matrix))