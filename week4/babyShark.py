from collections import deque

INF = 999999
n = int(input())
board = []
shark_x = 0
shark_y = 0
shark_size = 2

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 9:  # save shark position
            shark_y = i
            shark_x = j
            board[i][j] = 0  # makes shark pos 0 -> 나중에 자기랑 같은 크기 만날 때 지나갈 수 있음
# up left down right
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def bfs():
    dis = [[-1] * n for _ in range(n)]  # distance
    q = deque()
    q.append((shark_x, shark_y))

    dis[shark_y][shark_x] = 0

    while q:
        pos = q.popleft()
        x = pos[0]
        y = pos[1]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:  # in the boundary
                if shark_size >= board[next_y][next_x] and dis[next_y][next_x] == -1:
                    dis[next_y][next_x] = dis[y][x] + 1
                    q.append((next_x, next_y))

    return dis


def find(dis):
    y = -1
    x = -1
    result = INF

    for i in range(n):
        for j in range(n):
            if shark_size > board[i][j] and board[i][j] >=1 and dis[i][j] != -1:  # smaller than shark and reachable
                if result > dis[i][j]:
                    result = dis[i][j]
                    x, y = j, i

    if y == -1 and x == -1:
        return None

    else:
        return x, y, result


count = 0
ate=0

while True:

    value = find(bfs())

    if value is None:
        print(count)
        break

    else:
        shark_x, shark_y = value[0], value[1]
        count += value[2]
        board[shark_y][shark_x] = 0
        ate += 1

    if ate >= shark_size:
        shark_size += 1
        ate = 0
