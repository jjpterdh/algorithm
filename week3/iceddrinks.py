import sys

# input=sys.stdin.readline

# 상 하 좌 우
dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]


def solution(graph, n,m):
    count=0
    for i in range(m):
        for j in range(n):
            if graph[j][i]==1:
                continue
            
            count+=1
            graph[j][i]=1
            dfs(graph, i, j, n, m)

            
            # print(graph)

    return count

def dfs(graph, x,y,n,m):

    
    
    for i in range(4):
        # 상 하 좌 우 
        tmp_y=y+dy[i]
        tmp_x=x+dx[i]

        if tmp_y<0 or tmp_y >=n or tmp_x < 0 or tmp_x >=m:
            continue
        else:
            wall=graph[tmp_y][tmp_x]
            if wall==0:
                graph[tmp_y][tmp_x]=1
                dfs(graph, tmp_x, tmp_y, n, m)

    


    

# input 
n, m=map(int, input().split())


# ex
graph=[
    [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
    [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
    [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
]
# graph=[]
# for i in range(n):
#     graph.append(list(map(int, input())))


anw=solution(graph, n, m)
print(anw)
