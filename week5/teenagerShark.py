import copy

INF=1e9
board=[]
dir=[]
fishes=[]

for i in range(4):
    fishes.append(list(map(int, input().split())))

for i in range(4):
    b=[]
    d=[]
    for j in range(8):
        if j%2==0:
            b.append(fishes[i][j])
        else:
            d.append(fishes[i][j])

    board.append(b)
    dir.append(d)


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]




def fish_move(shark_x, shark_y, new_board, directions):
    n = 1
    # 리스트 복사
    update_board = copy.deepcopy(new_board)
    directions = copy.deepcopy(directions)


    while n <= 16:
        if n in eaten_fish:

            n += 1
        else:
            for i in range(4):
                for j in range(4):
                    if update_board[i][j] == n: # with order (small -> big)
                        # try all the directions
                        n += 1
                        # direction = directions[i][j]-1
                        direction = directions[i][j]
                        for k in range(direction, direction+9):
                            # 이동할 자리 확인
                            nx = j + dx[(k-1) % 8]
                            ny = i + dy[(k-1) % 8]

                            if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and (nx != shark_x or ny != shark_y): # in the boundary and no shark
                                # switch fish and directions
                                tmp_dir = directions[ny][nx]
                                directions[ny][nx] = k % 8
                                directions[i][j] = tmp_dir

                                tmp_fish = update_board[ny][nx]
                                update_board[ny][nx] = update_board[i][j]
                                update_board[i][j] = tmp_fish

                                break
                            else:
                                continue

    return update_board, directions


def dfs(x,y, board, directions):
    # 상어 움직임, 물고기가 없는 칸 이동 불가능
    # 물고기 이동

    #리스트 복사
    board=copy.deepcopy(board)
    directions=copy.deepcopy(directions)

    #해당 좌표 먹음
    eaten_fish.append(board[y][x])
    sum = board[y][x]
    board[y][x] = 0

    # 물고기 움직임
    board, directions = fish_move(x, y, board, directions)

    # 상어 좌표 방향 업데이트
    shark_direction = directions[y][x]-1

    nx = x
    ny = y
    while True:
        nx = nx + dx[shark_direction]
        ny = ny + dy[shark_direction]
        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
            if board[ny][nx]!=0:
                sum = max(sum, dfs(nx, ny, board, directions))
            else:
                continue


        else:
            break



    sum2=0
    for ele in eaten_fish:
        sum2+=ele

    eaten_fish.pop()

    return max(sum,sum2)




#initial shark x,y

eaten_fish=[]
print(dfs(0, 0, board, dir))



