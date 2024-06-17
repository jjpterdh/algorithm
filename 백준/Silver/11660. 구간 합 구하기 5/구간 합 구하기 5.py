import sys


input=sys.stdin.readline


n,m=map(int, input().split())

graph=[[0]*(n+1)]
summed=[[0]*(n+1) for _ in range(n+1)]


for i in range(n):
    graph.append([0]+list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,n+1):
        summed[i][j]=graph[i][j]+summed[i-1][j]+summed[i][j-1]-summed[i-1][j-1]

for _ in range(m):
    y1,x1,y2,x2=map(int, input().split())
    answer=summed[y2][x2]+summed[y1-1][x1-1]-summed[y2][x1-1]-summed[y1-1][x2]
    print(answer)

# print(summed)