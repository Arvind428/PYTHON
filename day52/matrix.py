m1=[[1,2,3],
    [3,3,6],
    [3,4,5]]
m2=[[2,3,5],
    [4,5,7],
    [8,4,2]]
rows=3
col=3
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(rows):
    for j in range(col):
        res[i][j]=m1[i][j]+m2[i][j]

print(res)