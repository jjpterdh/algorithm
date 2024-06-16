# 백준 # 11660

n, m=map(int, input().split())
mat=[ list(map(int, input().split())) for _ in range(n)]
sum_mat=[[0]*n for _ in range(n)]

sum_mat[0][0]=mat[0][0]
for i in range(1, n):
    
    sum_mat[i][0]=mat[i][0]+sum_mat[i-1][0]
    sum_mat[0][i]=mat[0][i]+sum_mat[0][i-1]



for i in range(1, n):
    for j in range(1, n):
        sum_mat[i][j]=sum_mat[i-1][j]+sum_mat[i][j-1]+mat[i][j]-sum_mat[i-1][j-1]


for i in range(m):
    y1,x1, y2,x2 = map(int, input().split())

    if x1>1 and y1>1:
        total=sum_mat[y2-1][x2-1]-sum_mat[y1-2][x2-1]-sum_mat[y2-1][x1-2]+sum_mat[y1-2][x1-2]
    
    elif x1==1 and y1==1:
        total=sum_mat[y2-1][x2-1]
    
    elif x1>1 and y1<=1:
        total=sum_mat[y2-1][x2-1]-sum_mat[y1-1][x1-2]
    
    elif x1<=1 and y1>1:
        total=sum_mat[y2-1][x2-1]-sum_mat[y1-2][x1-1]

    print(total)

    # print(y1, x1, y2, x2)
    
