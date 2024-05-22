import sys
from collections import deque
dy=[-1,0,0,1]
dx=[0,-1,1,0]

n,m=map(int ,input().split())
board=[[0]*(n+1)]
shops=[[0]]
pos=[[]]
npos=[[]]
out=0
for i in range(n):
    board.append([0]+list(map(int, input().split())))

for i in range(m):
    y, x=map(int, input().split())
    board[y][x]=2 
    shops.append((y, x))


    
def bfs(idx, y, x):
    sy,sx=shops[idx]
    visited=[[sys.maxsize]*(n+1) for _ in range(n+1)]
    visited[y][x]=0
    queue=deque([(y, x)])
    while queue:
        y, x=queue.popleft()

        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny<=0 or ny>n or nx<=0 or nx>n:
                continue
        
            if board[ny][nx]==5: # 이미 점령된 베이스 또는 편의점
                continue

            if visited[ny][nx]==sys.maxsize:
                visited[ny][nx]=visited[y][x]+1
                queue.append([ny, nx])
    

    return visited[sy][sx]

def select_base(idx):
    min_dis=sys.maxsize
    by,bx=0,0


    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]==1:
        
                # dis=cal_dis(i, j, sy, sx)
                dis=bfs(idx, i,j)
                if dis<min_dis:
                    by=i
                    bx=j
                    min_dis=dis

    # 베이스 캠프 점령
    board[by][bx]=5

    # 베이스로 이동한 사람 움직이 물르기
    for l in range(1,len(pos)):
        y,x=npos[l]
        if y==by and x==bx:
            move(l)

    return (by, bx)

def move(idx):
    y, x=pos[idx]
    dis=bfs(idx, y, x)
    

    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]

        if ny<=0 or ny>n or nx<=0 or nx>n:
            continue
        
        if board[ny][nx]==5: # 이미 점령된 베이스 또는 편의점
            continue

        new_dis=bfs(idx,ny,nx)
        
        if dis>new_dis: # 편의점을 향해 전진
            dis=new_dis
            npos[idx]=[ny,nx]
            



time=0
ppl=0
while True:
    time+=1
    
        
    # 1. 움직임
    # 보드에 있는 사람이 1명 이상
    length=min(time, len(pos))
    for l in range(1,length):
        if pos[l][0]==0: # 이미 도착한 사람                
            continue
        move(l)
    
    
    # 2. 점령된 베이스 또는 편의점 찾기
    for l in range(1,length):
        y,x=npos[l]
        sy,sx=shops[l]
        
        if y==sy and x==sx:
            board[y][x]=5
            pos[l]=[0,0]
            npos[l]=[0,0]
            out+=1
    
    # 사람 유입
    if time<=m:
        # 3. 베이스 캠프 차지
        ppl+=1
        pos.append(select_base(time))
        npos.append(pos[-1])
        # print(pos)

    pos=npos[:]
    # print(pos)

    # 4. 모든 사람 편의점 도착 -> 끝
    if out>=m:
        break

print(time)