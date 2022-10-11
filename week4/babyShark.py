from collections import deque
INF=9999999
n= int(input())


count=INF

board=[]
fish=[0,0,0,0,0,0,0] # 1~6 물고기 개수
fish_pos=[[] for _ in range(8)] # 상어보다 작은 물고기들의 좌표
food=deque()


visited=[[False]*n for _ in range(n)]
shark_size = 2


dy=[-1, 0, 0, 1]
dx=[0, -1, 1, 0]

time=INF
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j]==9: # save shark pos
            shark_y=i
            shark_x=j
        elif board[i][j]>=1:
            fish[board[i][j]]+=1 # save 물고기 크기별 개수
            fish_pos[board[i][j]].append((j,i))




# def shortest_distance(shark_x, shark_y):
#     # 가까운 물고기 계산
#     # 상어보다 작은 물고기 크기 계산
#     fish_x=INF
#     fish_y=INF
#
#     for i in range(1, shark_size):
#         for x,y in fish_pos[i]:
#             if not visited[y][x]:
#                 dx=shark_x-x
#                 dy=shark_y-y
#                 # 음수 양수 변환
#                 if dx < 0:
#                     dx = -dx
#                 if dy < 0:
#                     dy = -dy
#
#                 fish_x=min(fish_x,shark_x-x)
#                 fish_y=min(fish_y,shark_y-y)
#
#
#
#
#     # 가까운 물고기 좌표 반환
#     return (fish_x, fish_y)


def bfs(x, y, level_up):

    while food:

        print(food)
        if board[y][x] < shark_size and board[y][x]!=0: # 자기보다 작은 물고기를 만난 경우
            visited[y][x]=True
            level_up-=1
            if level_up==0: # 상어 진화
                shark_size+=1
                level_up=shark_size

        for i in range(4): #거리가 동일할 때 먹는 순서 => 상 좌 우 하
            next_x = x+dx[i]
            next_y = y+dy[i]

            if next_x <0 or next_x >=n or next_y<0 or next_y >=n: # out of boundary
                continue

            if board[next_y][next_x] <= shark_size:
                count += bfs(next_x, next_y, count+1)












def solve():
    global shark_size, visited, fish_pos, food, count


    for i in range(1, shark_size):
        for x,y in fish_pos[i]:
            food.append((x,y))

    print(food)
    food.sort()
    print(food)
    # bfs(shark_x,shark_y, 0)










print(count)