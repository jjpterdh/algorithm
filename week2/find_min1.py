# 백준 #11003
from collections import deque



n,l=map(int, input().split())
arr=list(map(int, input().split()))

queue=deque([])


front=0
end=0
for i in range(n):

    # if queue is empty
    while queue and queue[-1][1] > arr[i]:
        queue.pop()
    
    queue.append((i,arr[i]))
    
    
        
    
    if queue[0][0]< i-l+1:
        queue.popleft()
        end-=1

    print(queue[0][1], end=' ')
    # print(queue[0], end=' ')


