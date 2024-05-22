import sys
from queue import PriorityQueue
from collections import deque
input=sys.stdin.readline



# 좌상 상 우상, 좌, 우, 좌하, 하, 우하
dy=[-1, -1, -1, 0,0,1,1,1]
dx=[-1,0,1,-1,1,-1,0,1]

# 산타: 상 우 하 좌
sy=[-1, 0, 1, 0]
sx=[0, 1, 0, -1]

# 입력
n,m,p,c,d=map(int, input().split())
ry,rx=map(int, input().split())


# 초기 변수 설정
graph=[[0 for i in range(n+1)] for j in range(n+1)]
graph[ry][rx]='r'
santa_pos=deque([[0,0] for _ in range(p+1)])
santa_point=[0]*(p+1)
survived=[True]*(p+1)
survived[0]=False
rest=[0]*(p+1)
# 산타 입력
for i in range(p):
    idx, y, x=map(int, input().split())
    graph[y][x]=idx
    # santa_pos.append([y,x])
    santa_pos[idx][0]=y
    santa_pos[idx][1]=x

# 거리 계산
def cal_dis(y1, x1, y2, x2):
    y=y1-y2
    x=x1-x2
    return y*y+x*x

# 충돌
def collision(santa, idx):
    if santa:
        santa_point[idx]+=d
        rest[idx]=1
    else:
        santa_point[idx]+=c
    
        rest[idx]=2



# 상호작용
def interaction(y, x, dir, idx, santa):
    if graph[y][x]==0 or graph[y][x]==idx:
        graph[y][x]=idx
        return
    else:
        tmp=graph[y][x]

        # 현재 산타로 대치
        graph[y][x]=idx
        santa_pos[idx][0]=y
        santa_pos[idx][1]=x

        # 기존 산타의 반대방향으로 이동
        if santa:
            ny=y-sy[dir]
            nx=x-sx[dir]

        # 루돌프가 밀친 방향으로
        else:
            ny=y+dy[dir]
            nx=x+dx[dir]

        santa_pos[tmp][0]=ny
        santa_pos[tmp][1]=nx

        # 밖으로 아웃되면 탈락
        if ny<=0 or ny>n or nx<=0 or nx>n:
            survived[tmp]=False
            return
        
    
        interaction(ny, nx, dir, tmp, santa)
    

# 움직임
def move(y, x, santa):
    if santa: # 4가지 방향

        # 현재거리 계산
        min_dis=cal_dis(y, x, ry, rx)
        npos=[y,x]

        # 상 우 하 좌
        for i in range(4):
            ny=y+sy[i]
            nx=x+sx[i]

            if ny<=0 or ny>n or nx<=0 or nx>n:
                continue

            elif graph[ny][nx]!=0 and graph[ny][nx]!='r': # 이미 다른 산타 존재
                continue

            dis=cal_dis(ny, nx, ry, rx)

            if min_dis>dis and dis!=0:
                min_dis=dis
                npos[0]=ny
                npos[1]=nx
                
            # 충돌
            elif dis==0:
                # print("santa hit")
                collision(True, santa)
                ny-=(d*sy[i])
                nx-=(d*sx[i])

                # 산타 아웃
                if ny<=0 or ny>n or nx<=0 or nx>n:
                    survived[santa]=False
                    npos[0]=0
                    npos[1]=0
                else:
                    npos[0]=ny
                    npos[1]=nx 
                    # 상호작용
                    interaction(ny, nx, i, santa, True)
        
        graph[y][x]=0
        return npos
    
    else: # 루돌프 움직임 8가지 방향
        min_dis=sys.maxsize
        npos=[0,0]
        
        # 산타와 거리 비교해서 최소거리 찾기
        for i in range(n,0,-1):
            for j in range(n, 0, -1):
                if i==y and j==x:
                    continue
                
                if graph[i][j]!='r' and graph[i][j]!=0: # 산타 위치 확인
                
                    dis=cal_dis(y, x, i, j)
                    if min_dis>dis:
                        min_dis=dis
                        
                        # 산타 위치 저장
                        npos[0]=i
                        npos[1]=j
                

        nry=0
        nrx=0
        for i in range(8):
            ny=y+dy[i]
            nx=x+dx[i]

            
            # 지도 밖이면 continue            
            if ny<=0 or ny>n or nx<=0 or nx>n:
                continue

            dis=cal_dis(ny, nx, npos[0],npos[1])
            if min_dis>dis:
                min_dis=dis
                
                # 루돌프 위치 저장
                nry=ny
                nrx=nx

                # 충돌
                if dis==0:
                    idx=graph[ny][nx]
                    collision(False, idx)
                    
                    ny+=c*(dy[i])
                    nx+=c*(dx[i])
                    if ny<=0 or ny>n or nx<=0 or nx>n:
                        survived[idx]=False
                    else:
                        
                        santa_pos[idx][0]=ny
                        santa_pos[idx][1]=nx
                        # 상호작용
                        interaction(ny, nx, i, idx, False)

        graph[y][x]=0
        


        return (nry, nrx)
    



for _ in range(m):
    
    #루돌프 움직임
    npos=move(ry, rx, False)
    graph[npos[0]][npos[1]]='r'
    ry=npos[0]
    rx=npos[1]
    # print(santa_point)
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         print(graph[i][j], end=' ')
    #     print()

    # print("------------------")
   
    # 산타 움직임
    for i in range(1,p+1):
        if survived[i] and rest[i]==0:
            y,x=santa_pos[i]
            npos=move(y, x, i)
            # 산타 위치 업데이트
            graph[npos[0]][npos[1]]=i
            santa_pos[i][0]=npos[0]
            santa_pos[i][1]=npos[1]
        
        elif rest[i]:
            rest[i]-=1
    
    
    # print(santa_point)
    # for i in range(1, n+1):
    #     for j in range(1, n+1):
    #         print(graph[i][j], end=' ')
    #     print()
    
    # print()
    # print(santa_pos)
    # print(survived)
    if not True in survived:
        break

    for i in range(1,p+1):
        if survived[i]:
            santa_point[i]+=1
        
    

for i in range(1,p+1):
    print(santa_point[i], end=' ')