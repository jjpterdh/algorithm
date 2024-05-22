import sys
from collections import deque
input=sys.stdin.readline

n,l=map(int, input().split())
arr=list(map(int, input().split()))
d=deque()

for i in range(n):
    while d and d[-1][0] > arr[i]:
        d.pop()
    d.append((arr[i], i))
    if d[0][1] <= i-l:
        d.popleft()
    print(d[0][0], end=' ')