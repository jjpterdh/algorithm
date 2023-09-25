#이것이 코딩테스트다 

# 상 우 하 좌
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

# 현재 방향에서 왼쪽 방향으로 틀고 시작

# 1: 바다 0: 육지

# input
# n,m=map(int, input().split())

# chara=list(map(int, input().split()))

# visited=[]
# graph=[]
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     visited.append(list())
#     for j in range(m):
#         visited[i].append(False)

n,m=4, 4
y, x, dir=1, 1, 0
graph=[
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
visited=[
    [False]*m for _ in range(n)
]

count=1

# y, x=chara[0], chara[1]
# dir=chara[2]



count_dir=0
while True:
    dir=(dir+1)%4
    
    nx=x+dx[dir]
    ny=y+dy[dir]


    if nx<0 or nx>=m or ny<0 or ny >=n: # out of map
        continue
    
 
    if graph[ny][nx]==0 and count_dir==0 and visited[ny][nx]==False: # 육지 + 방문 x
        x=nx
        y=ny
        count+=1
        visited[ny][nx]=True
        count_dir=0
        

    elif graph[ny][nx]==0 and count_dir<3: # 육지 + 방문
        count_dir+=1

    elif graph[ny][nx]==0 and count_dir>3: # 4방향 다 막힘
        
        nx=nx-dx[dir]
        ny=ny-dy[dir]

        if nx<0 or nx>=m or ny<0 or ny >=n: # out of map
            break
        
        elif graph[ny][nx]==1: # 바다
            break

        x=nx
        y=ny
        count_dir=0
    

    elif graph[ny][nx]==1 and count_dir>0: # 바다일 경우
        break

    else:
        count_dir+=1
    



print(count)

# 문제 이해를 못함
# 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면?
