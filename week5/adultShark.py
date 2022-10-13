# n은 보드 크기, m은 상어개수, k는 냄새 지속시간
n,m,k=map(int, input().split())

#initial setting
board=[ list(map(int,input().split())) for _ in range(n)]
scent_board=[[0]*n for _ in range(n)]

for i in range(n*n):
    x=i%n
    y=i//n
    if board[y][x] !=0:
        scent_board[y][x] = [board[y][x], k]

shark = [list(map(int, input().split()))] # 시작 방향

shark_directions=[[list(map(int, input().split())) for _ in range(4)]]*m

print(scent_board)


count=0
# 위 아래 왼쪽 오른쪽
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def update_scent_board(scent_board):

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0: # 상어가 있을 시 향 업데이트
                scent_board[i][j]=[board[i][j], k]
            if scent_board[i][j] != 0 and board[i][j] == 0: # 상어가 없는 곳은 k-1
                if scent_board[i][j][1]-1 <= 0:
                    scent_board[i][j][1] = 0
                else:
                    scent_board[i][j][1] -= 1


def bfs():
    total = 0

    count = max(total, count)
    return

def remove_shark(board, x, y):

    board[y][x] = 0
    return

def find_shark(board, num):
    for i in range(n):
        for j in range(n):
            if board[i][j]==num:
                return j, i
    return None


def shark_move():
    global count
    bfs()




#
#
#



