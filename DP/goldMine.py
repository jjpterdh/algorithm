# 이것이 코딩테스트다

n,m=map(int, input().split())

a=[[0]*m for _ in range(n)]

d1=list(map(int, input().split()))
d=[]
index=0
for i in range(n):
    d.append(d1[index:index+m])
    index+=m




# 왼쪽 위, 왼쪽, 왼쪽 아래
dy=[-1, 0, 1]
dx=[-1, -1, -1]

for i in range(1, m):
    for j in range(n):
        if a[j][i]==0:
            left_up=d[j][i]
            left=d[j][i]
            left_down=d[j][i]

            if j==0: # 맨 위쪽
                left+=d[j][i-1]
                left_down+=d[j+1][i-1]
            
            elif j==n-1: # 맨 아래
                left+=d[j][i-1]
                left_up+=d[j-1][i-1]
            
            else: # 중간
                left_up+=d[j-1][i-1]
                left+=d[j][i-1]
                left_down+=d[j+1][i-1]



            d[j][i]=max(
                left_up, left, left_down
            )
            a[j][i]=d[j][i]
        else: continue


anw=0
for i in range(n):
    anw=max(anw, d[i][m-1])

print(anw)
    
    




