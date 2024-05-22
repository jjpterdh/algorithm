from collections import deque
n=int(input())

arr=deque([_ for _ in range(n,0,-1)])

while len(arr)>1:
    arr.pop()
    arr.appendleft(arr[-1])
    arr.pop()

print(arr[-1])