INF = 9999999

n, m = map(int, input().split())

safe = 0
virus_area = INF

graph = []
virus = []  # (x,y)
visited = [[False]*m for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# up down left right


for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((j, i))  # save pos of virus (x,y)
        elif graph[i][j] == 0:  # 안전구역 저장
            safe += 1



def spread(y, x):
    v_area = 1
    visited[y][x] = True

    for k in range(4): # up down left right
        next_y = y + dy[k]
        next_x = x + dx[k]


        if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:  # out of boundary
            continue

        if graph[next_y][next_x] == 0 and (not visited[next_y][next_x]):  # 빈칸 & 감염 되지 않은 지역
            v_area += spread(next_y, next_x)

    return v_area


def dfs():
    v_area = 0
    for x, y in virus:
        v_area += spread(y, x)

    return v_area


def solve(start, wall):
    global virus_area, visited

    if wall == 3:
        visited = [[False]*m for _ in range(n)]

        virus_area = min(virus_area, dfs())

        return

    for i in range(start, n * m):
        y = i // m
        x = int(i % m)

        if graph[y][x] == 0:
            graph[y][x] = 1
            solve(i + 1, wall + 1)
            graph[y][x] = 0


solve(0, 0)
safe-=3 # 벽 3개 세워야함
virus_area-=len(virus)
print(safe - virus_area)


# reference: https://jeongchul.tistory.com/672
