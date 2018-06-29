#Write an algorithm such that if an element in an Matrix is 0, its entire row and columns are set to 0.
import random

def init_matrix(m,n):
    if min(m,n)<1:
        print("incorrect input")
        exit()
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(str(i)+str(j))
    return matrix

def print_matrix(matrix):
    if matrix:
        for n in range(len(matrix)):
            for m in range(len(matrix[n])):
                print(matrix[n][m], end = ' ')
            print()
    print()

def add_few0(matrix):
    zn = random.randrange(1,len(matrix))
    print("adding",zn,"zero(s) to the matrix: [please consider XX as zero for readability purpose]")
    for _ in range(zn):
        y = random.randrange(len(matrix))
        x = random.randrange(len(matrix[y]))
        matrix[y][x] = "XX"
        print("(",x,",",y,")",sep='',end='')
    print(); print()
    return matrix

def set_col_0(matrix,col):
    for row in range(len(matrix[col])):
        matrix[col][row] = "XX"

def set_row_0(matrix,row):
    for col in range(len(matrix)):
        matrix[col][row] = "XX"

def zerofy(matrix):
    ylen = len(matrix)
    xlen = len(matrix[0])
    rows0 = set()
    cols0 = set()
    for y in range(ylen):
        for x in range(xlen):
            if matrix[y][x] == "XX":
                rows0.add(x)
                cols0.add(y)
    for r in rows0:
        set_row_0(matrix,r)
    for c in cols0:
        set_col_0(matrix,c)
    return matrix


m1 = init_matrix(5,4)
m1 = add_few0(m1)
m1 = zerofy(m1)
print_matrix(m1)