# 백준 뱀 3190번

from collections import deque

n= int(input())
k=int(input())


board=[[0]*n for _ in range(n)]
board[0][0]=1

for i in range(k):
    y,x= map(int, input().split())

    board[y-1][x-1]=2


l=int(input())
moves=deque([])
counts=deque([])
for i in range(l):
    t,m=input().split()
    counts.append(int(t))
    moves.append(m)

counts.append(100000)
moves.append("END")

# 오른쪽, 아래, 왼쪽, 위
dy=[0, 1, 0, -1]
dx=[1, 0, -1, 0]

# 뱀 방향: 초기 오른쪽
flag=0 


def turn_left(flag):
    flag-=1
    if flag<0:
        flag=3
    return flag

def turn_right(flag):
    return (flag+1)%4




time=0
H=(0,0)
T=(0,0)

c=counts.popleft()
m=moves.popleft()

snake=deque([(0,0)])
while True:
    time+=1
    
    # snake turn direction
    
    if c<time and counts:
        if m=='L':
            flag=turn_left(flag)
        else:
            flag=turn_right(flag)
        
        c=counts.popleft()
        m=moves.popleft()

    # snake move
    
    ny=H[0]+dy[flag]
    nx=H[1]+dx[flag]

    # hit by wall
    if ny < 0 or ny >=n or nx<0 or nx >=n:
        break
    
    # hit by itself
    elif board[ny][nx]==1:
        break

    # eat apple
    H=(ny,nx)
    snake.append(H)

    if board[ny][nx]==2:
        board[ny][nx]=1
        
    
    # x eat apple
    else:
        T=snake.popleft()
        board[ny][nx]=1
        board[T[0]][T[1]]=0
        
        # change Tail position
        

            
    # print("----------------------")
    # for i in range(n):
    #     print(board[i])


print(time)

    
    
# 37분 56초