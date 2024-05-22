from collections import deque
dy=[-1, 1, 0,0]
dx=[0,0,-1,1]
def maze(maps, sx,sy, m,n, target):
    visited=[[False]*n for _ in range(m)]
    queue=deque([(sy, sx, 0)])
    count=0
    visited[sy][sx]=True
    while queue:
        y,x, count=queue.popleft()
        

        
        if maps[y][x]==target:
            return count
        
        

        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            
            if ny<0 or ny>=m or nx<0 or nx>=n or visited[ny][nx] or maps[ny][nx]=="X":
                continue

            # visited 는 무조건 이때 추가하기
            visited[ny][nx]=True
            queue.append((ny, nx, count+1))
        
        
    

    return -1

def solution(maps):
    answer = 0
    m,n=len(maps), len(maps[0])
    sy,sx=0,0
    ly, lx=0,0
    for i in range(m):
        for j in range(n):
            if maps[i][j]=='S':
                sy=i
                sx=j
            
            elif maps[i][j]=='L':
                ly=i
                lx=j
    
    path1=maze(maps, sx, sy,m,n, 'L')
    path2=maze(maps, lx, ly, m ,n ,'E')
    
    if path1!=-1 and path2!=-1:
        answer=path1+path2
        return answer
    else:
        return -1
    





maps=["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))