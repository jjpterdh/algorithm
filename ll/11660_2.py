import sys
input=sys.stdin.readline


n, m = map(int,input().split())

graph=[[0]*(n+1)]
sum_graph=[[0 for i in range(n+1)] for _ in range(n+1)]
for i in range(n):
    graph.append([0]+list(map(int, input().split())))



for i in range(1, n+1):
    for j in range(1, n+1):
        sum_graph[i][j]=sum_graph[i-1][j]+sum_graph[i][j-1]-sum_graph[i-1][j-1]+graph[i][j]



for _ in range(m):
    y1, x1, y2, x2=map(int, input().split())
    ans=sum_graph[y2][x2]-sum_graph[y1-1][x2]-sum_graph[y2][x1-1]+sum_graph[y1-1][x1-1]
    print(ans)
