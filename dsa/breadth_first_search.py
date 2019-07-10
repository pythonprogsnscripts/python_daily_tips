r_max = int(input())
c_max = int(input())
matrix = []
for scan in range(r_max):
    matrix.append(list(map(int , input().split())))
print(matrix)

def check(matrix, row, col):
    if row < 0 or col == r_max or col >= c_max:
        print('in first condition')
        return 0
    if matrix[row][col] == 0:
        print('in second condition')
        return 0
    matrix[row][col] = 0
    size = 1
    for k in range(row-1,row+2):
        for d in range(col-1, col+2):
            if k != row or d != col:
                size += check(matrix,k,d)

    return size

max_reg = 0

for row in range(r_max):
    for col in range(c_max):
        print(row,',',col,'--->',matrix[row][col])
        if matrix[row][col] == 1:
            print('matrix row or col is 1')
            size = check(matrix,row,col)
            max_reg = max(size, max_reg)

print(max_reg)