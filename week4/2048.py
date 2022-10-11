#max movement: 5
#output: the biggest block
from collections import deque

n= int(input())

block=[]
for i in range(n):
    block.append(list(map(int, input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
#right, left, down, up

arr=deque()
def movements(dir):




    # for i in range(n):
    #     for j in range(n):
    #         if i+dy[dir] <0 or i+dy[dir] >=n or j+dx[dir] <0 or j+dx[dir] >=n: # out of boundary
    #             continue
    #
    #         if block[i][j]==block[i+dy[dir]][j+dx[dir]]: #가는 방향의 블록이랑
    #             block[i+dy[dir]][j+dx[dir]]*=2


def merge(i, j, di, dj):

