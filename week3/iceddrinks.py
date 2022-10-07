def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[y][x]==0:
        graph[y][x]=1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    
    return False


n,m=map(int, input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))



dfs(0,0)