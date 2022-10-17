from copy import deepcopy
from sys import stdin
input = stdin.readline

n = int(input())
pan = [ list(map(int, input().split())) for _ in range(n) ]
answer = 0

def up(pan):
    for x in range(n):
        p = 0

        for y in range(1, n):
            if pan[y][x]:
                tmp = pan[y][x]
                pan[y][x] = 0

                if pan[p][x] == 0:
                    pan[p][x] = tmp
                elif pan[p][x] == tmp:
                    pan[p][x] *= 2
                    p += 1
                else:
                    p += 1
                    pan[p][x] = tmp
    return pan

def down(pan):
    for x in range(n):
        p = n-1

        for y in range(n-2, -1, -1):
            if pan[y][x]:
                tmp = pan[y][x]
                pan[y][x] = 0

                if pan[p][x] == 0:
                    pan[p][x] = tmp
                elif pan[p][x] == tmp:
                    pan[p][x] *= 2
                    p -= 1
                else:
                    p -= 1
                    pan[p][x] = tmp
    return pan

def left(pan):
    for x in range(n):
        p = 0

        for y in range(1, n):
            if pan[x][y]:
                tmp = pan[x][y]
                pan[x][y] = 0

                if pan[x][p] == 0:
                    pan[x][p] = tmp
                elif pan[x][p] == tmp:
                    pan[x][p] *= 2
                    p += 1
                else:
                    p += 1
                    pan[x][p] = tmp

    return pan

def right(pan):
    for x in range(n):
        p = n-1

        for y in range(n-2, -1, -1):
            if pan[x][y]:
                tmp = pan[x][y]
                pan[x][y] = 0

                if pan[x][p] == 0:
                    pan[x][p] = tmp
                elif pan[x][p] == tmp:
                    pan[x][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    pan[x][p] = tmp
    return pan

def dfs(pan, depth):
    global answer

    if depth == 5:
        for i in range(n):
            for j in range(n):
                answer = max(pan[i][j], answer)
        return

    dfs(up(deepcopy(pan)), depth+1)
    dfs(down(deepcopy(pan)), depth + 1)
    dfs(left(deepcopy(pan)), depth + 1)
    dfs(right(deepcopy(pan)), depth + 1)

dfs(pan, 0)
print(answer)