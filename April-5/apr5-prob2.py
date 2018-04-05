A = [[3, 5, 6],[4, 8, 10],[2, 1, 8]]
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

Res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
    for j in range(len(I[0])):
        for k in range(len(I)):
            Res[i][j] += A[i][k] * I[k][j]
            
print(Res)
if(A == Res):
    print("Therefore, A = A.I")