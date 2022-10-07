from collections import deque
n,m = map(int , input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))



def bfs(y,x):
    queue=deque()
    queue.append([y,x])
    
    dx=[1,-1,0, 0]
    dy=[0,0,1,-1]


    
    
    while queue:
        pos=queue.popleft()
        x=pos[1]
        y=pos[0]
        
        
        if pos[0]==n-1 and pos[1]==m-1:
            break

        #check up down left right
        for i in range(4):
            if x+dx[i]>=0 and x+dx[i] <m and y+dy[i] >=0 and y+dy[i] <n: 
                if graph[y+dy[i]][x+dx[i]]>=1:
                    graph[y+dy[i]][x+dx[i]]= graph[y][x]+1
                    queue.append((y+dy[i],x+dx[i]))
                
    
    return graph[n-1][m-1]

    
    
    

print(bfs(0,0))
