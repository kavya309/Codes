r=int(input())
c=int(input())
matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
         print(matrix[i][j], end=" ")
    print()
                 
