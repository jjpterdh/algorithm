# n은 보드 크기, m은 상어개수, k는 냄새 지속시간
n,m,k=map(int, input().split())

#initial setting
board=[ list(map(int,input().split())) for _ in range(n)]
scent_board=[[0]*n for _ in range(n)] # shark_level, scent_k


for i in range(n):
    for j in range(n):
        if board[i][j] !=0:
            scent_board[i][j]=[board[i][j],k]

shark = list(map(int, input().split())) # 상어의 현재 방향 저장 m 개
out_shark=[]
updated=[False]*m

shark_directions=[[list(map(int, input().split())) for _ in range(4)] for i in range(m)]

count=0

# 위 아래 왼쪽 오른쪽
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def update_scent_board():

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0: # 상어가 있을시 향 업데이트
                scent_board[i][j] = [board[i][j], k]
            if scent_board[i][j] != 0 and board[i][j] == 0: # 상어가 없는 곳은 k-1
                if scent_board[i][j][1]-1 <= 0:
                    scent_board[i][j] = 0
                else:
                    scent_board[i][j][1] -= 1



def remove_shark(ori_x,ori_y, new_x, new_y):
    # check if there are multiple sharks in same location
    out_shark.append(max(board[ori_y][ori_x], board[new_y][new_x]))
    board[ori_y][ori_x]= min(board[ori_y][ori_x], board[new_y][new_x])

    board[new_y][new_x] = 0

    return

def find_shark(x,y):
    if board[y][x] !=0:
        return True
    else:
        return False

def shark_move():
    # check sharks in board
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and not updated[board[i][j]-1]: # 상어 존재
                shark_level=board[i][j]-1

                # 해당 레벨 상어의 현재 방향 shark[shark_level]
                for k in range(4): # 4가지 방향 탐색
                    now_direction = shark_directions[shark_level][shark[shark_level]-1][k]-1

                    nx = j + dx[now_direction]
                    ny = i + dy[now_direction]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n: # out of boundary
                        continue

                    else: # in the boundary
                        if find_shark(nx,ny) and scent_board[ny][nx] ==0:# 점령하기 전
                            # 상어 싸우기

                            remove_shark(nx, ny, j, i)
                            updated[shark_level] = True
                            shark[shark_level] = now_direction+1
                            break
                        elif not find_shark(nx, ny) and scent_board[ny][nx]==0:# 빈 칸
                            # 상어 이동
                            board[ny][nx] = shark_level+1
                            board[i][j] = 0
                            updated[shark_level] = True
                            shark[shark_level] = now_direction+1
                            break
                        else:
                            continue

                # 갈 수 있는 방향 없을 때 왔던 곳으로 돌아가기
                if not updated[shark_level]: #자기 향이 있는 방향으로 잡기
                    for k in range(4):
                        now_direction = shark_directions[shark_level][shark[shark_level] - 1][k] - 1
                        nx = j + dx[now_direction]
                        ny = i + dy[now_direction]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:  # out of boundary
                            continue
                        else:
                            if scent_board[ny][nx] != 0 and (shark_level+1) == scent_board[ny][nx][0]: # 자기 향이 있는곳
                                board[ny][nx] = shark_level + 1
                                board[i][j] = 0
                                updated[shark_level] = True
                                shark[shark_level] = now_direction+1
                                break
                            else:
                                continue



while True:

    if len(out_shark) >= m-1 or count > 1000:
        break
    shark_move()


    update_scent_board()

    updated=[False]*m
    count+=1

if count>1000:
    print(-1)
else:
    print(count)
