import copy
#max movement: 5

n = int(input())
biggest_num = 0
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        biggest_num=max(biggest_num, board[i][j])

updated=[[False]*n for _ in range(n)]

# left, right, up, down
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def update_blocks(new_board, x,y, nx, ny):
    # 같은 번호인지 확인
    global biggest_num

    if new_board[y][x] == new_board[ny][nx] and not updated[ny][nx]:
        updated[ny][nx] = True
        new_board[ny][nx] *= 2
        new_board[y][x] = 0
        if biggest_num < new_board[ny][nx]:

            biggest_num = new_board[ny][nx]


    return

def update_board(uboard, dir, count):
    global updated
    updated=[[False]*n for _ in range(n)]

    new_board=copy.deepcopy(uboard)
    start, end, add = 0, n, 1

    if dir==0: # left
        

        for i in range(start, end): #left
            tmp_i=i
            for j in range(start, end):
                if new_board[j][i] != 0: # 번호가 존재할 시
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    while nx >= 0 and nx < n and ny >= 0 and ny < n: # in the boundary


                        if new_board[ny][nx] !=0: # 움직일 칸에 번호가 있을시
                            update_blocks(new_board, i, j, nx, ny)
                            break
                        else: #없을시
                            new_board[ny][nx] = new_board[j][i]
                            new_board[j][i] = 0
                        j = ny
                        i = nx
                        nx = nx+dx[dir]
                        ny = ny+dy[dir]
                i=tmp_i

    elif dir == 1:  # right

        start = n-1
        end = -1
        add = -1

        for i in range(start, end, add):
            tmp_i=i
            for j in range(start, end, add):
                if new_board[j][i] != 0:
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    while nx >= 0 and nx < n and ny >= 0 and ny < n: # in the boundary

                        if new_board[ny][nx] != 0:  # 움직일 칸에 번호가 있을시
                            update_blocks(new_board, i, j, nx, ny)
                            break
                        else:  # 없을시
                            new_board[ny][nx] = new_board[j][i]
                            new_board[j][i] = 0


                        j=ny
                        i=nx
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                i=tmp_i

    elif dir == 2: # up
        for i in range(start, end):
            tmp_i=i
            for j in range(start, end):
                if new_board[i][j] !=0 :
                    nx=j+dx[dir]
                    ny=i+dy[dir]
                    while nx >= 0 and nx < n and ny >= 0 and ny < n:  # in the boundary
                        if new_board[ny][nx] != 0:  # 움직일 칸에 번호가 있을시
                            update_blocks(new_board, j, i, nx, ny)
                            break
                        else:  # 없을시
                            new_board[ny][nx] = new_board[i][j]
                            new_board[i][j] = 0
                        j=nx
                        i=ny
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                i=tmp_i

    else: # down
        start=n-1
        end=-1
        add= -1
        for i in range(start, end, add):
            tmp_i=i
            for j in range(start, end, add):
                if new_board[i][j] != 0:
                    nx = j + dx[dir]
                    ny = i + dy[dir]
                    while nx >= 0 and nx < n and ny >= 0 and ny < n: # in the boundary

                        if new_board[ny][nx] != 0:  # 움직일 칸에 번호가 있을시
                            update_blocks(new_board, j, i, nx, ny)
                            break
                        else:  # 없을시
                            new_board[ny][nx] = new_board[i][j]
                            new_board[i][j] = 0
                        i=ny
                        j=nx
                        nx = nx + dx[dir]
                        ny = ny + dy[dir]
                i=tmp_i


    return new_board
def dfs(count, board):
    global n
    if count > 5:

        return

    new_board = copy.deepcopy(board)



    for dir in range(4):
            # 좌 우 상 하
            dfs(count + 1, update_board(new_board, dir, count))


    return

dfs(1, board)

print(biggest_num)