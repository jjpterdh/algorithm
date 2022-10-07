

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]==0: 
        graph[x][y]=1
        dfs(x,y-1) # 상
        dfs(x,y+1) # 하
        dfs(x-1,y) # 좌
        dfs(x+1,y) # 우
        return True
    
    
    return False


n,m=map(int, input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))


count=0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            count+=1

print(count)