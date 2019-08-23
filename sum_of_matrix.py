row=int(input("enter the num of row"))
col=int(input("enter the num of column"))
sum_mat=[[0,0,0],[0,0,0],[0,0,0]]
matrix1=[]
print('enter the value in matrix1')
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix1.append(a)
matrix2 = []
print('enter the value in matrix2')
for i in range(row):
    b = []
    for j in range(col):
        b.append(int(input()))
    matrix2.append(b)
print('matrix one')
for val in matrix1:
    for item in val:
        print(item,end=' ')
    print()
print('matrix2')
for value in matrix2:
    for items in value:
        print(items,end=' ')
    print()

for i in range(len(matrix2)):
    for j in range(len(matrix2)):
        sum_mat[i][j]=matrix1[i][j]+matrix2[i][j]

for values in sum_mat:
    for i in values:
        print(i,end='')
    print()