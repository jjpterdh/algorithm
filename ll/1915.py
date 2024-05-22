import sys

input=sys.stdin.readline
n,m=map(int, input().split())

graph=[list(input().strip()) for _ in range(n)]

d=[[0 for _ in range(m+1)] for _ in range(n+1)]
max_num=0
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i-1][j-1]=='1':
            d[i][j]=min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1
            max_num=max(max_num, d[i][j])

print(max_num*max_num)
