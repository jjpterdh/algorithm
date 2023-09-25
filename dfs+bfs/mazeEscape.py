from collections import deque
# input
n,m=map(int, input().split())

# 상 하 좌 우
dx=[0,0,1,-1]
dy=[-1,1,0,0]

# graph=[
#     [1,0,1,0,1,0],
#     [1,1,1,1,1,1],
#     [0,0,0,0,0,1],
#     [1,1,1,1,1,1],
#     [1,1,1,1,1,1]
# ]

graph=[
    [1,1,0],
    [0,1,0],
    [0,1,1]
]

# graph=[]
# for i in range(n):
#     graph.append(map(int, input()))

def solution(graph, n, m):
    
    
    count=bfs(graph, n,m)


    
    return count


def bfs(graph, n, m):
    queue=deque()
    queue.append((0,0))
    

    while queue:
        x,y= queue.popleft()
        for i in range(4):
            tmp_x=x+dx[i]
            tmp_y=y+dy[i]

            if tmp_x < 0 or tmp_x >=m or tmp_y<0 or tmp_y >=n:
                continue
            
            

            if graph[tmp_y][tmp_x]==1:
                graph[tmp_y][tmp_x]=graph[y][x]+1                
                queue.append((tmp_x,tmp_y))
            
            

            

            

    
    
    return graph[n-1][m-1]

anw=solution(graph,n,m)
print(graph)
print(anw)
