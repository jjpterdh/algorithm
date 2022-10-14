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


def 