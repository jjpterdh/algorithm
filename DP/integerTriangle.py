# 백준 1932번 정수 삼각형

n=int(input())

tri=[]
for _ in range(n):
    tri.append(list(map(int,input().split())))


max_value=0

for i in range(n-2, -1, -1):
    for j in range(i+1):
        max_value=max(tri[i+1][j], tri[i+1][j+1])
        tri[i][j]+=max_value

print(tri[0][0])



    
# time: 5분 43초
