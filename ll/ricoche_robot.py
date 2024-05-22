import sys
from collections import deque
sys.setrecursionlimit(10**6)
# 상 하 좌 우
dx=[0,0,-1,1]
dy=[-1,1,0,0]

inf=1e9

def bfs(board, dis, y, x):
    
    queue=deque([(y, x, 0)])
    

    while queue:
        y, x, score=queue.popleft()
        if board[y][x]=='G':
            return dis[y][x]
        

        score+=1
        for i in range(4):
            
            ny=y+dy[i]
            nx=x+dx[i]

            if ny<0 or ny>=len(board) or nx<0 or nx>=len(board[0])or board[ny][nx]=='D':
                continue
            nny=0
            nnx=0

            while ny>=0 and ny<len(board) and nx>=0 and nx<len(board[0]):
                if board[ny][nx]=='D':
                    break
                nny=ny
                nnx=nx

                ny+=dy[i]
                nx+=dx[i]
                
                    
            if dis[nny][nnx]>score:
                dis[nny][nnx]=score
                queue.append((nny,nnx, score))

    return -1

def solution(board):
    answer = 0
    sy,sx=0,0
    ey,ex=0,0
    dis=[[inf for i in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="R":
                
                sy=i
                sx=j
                dis[i][j]=0
            
    
    
    answer=bfs(board, dis, sy, sx)
    # for i in range(len(dis)):
    #     for j in range(len(dis[0])):
    #         if dis[i][j]==inf:
    #             print('x', end='\t')
    #         else:
    #             print(dis[i][j], end='\t')
    #     print()
    return answer


board=[".D.R", "....", ".G..", "...D"]
print(solution(board))