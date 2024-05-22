import sys
from collections import deque


input=sys.stdin.readline
computers={}
n,m=map(int, input().split())
ans=[0]*(n+1)


# 부모를 여러 개 가질 수 있어서 union and find 사용 불가.
def bfs(computers, i,n):
    visited=[False]*(n+1)
    queue=deque([i])
    visited[i]=True
    
    while queue:
        node=queue.popleft()
        if computers.get(node) is None:
            continue
        for com in computers[node]:
            if not visited[com]:
                visited[com]=True
                queue.append(com)
                ans[com]+=1
    return


for i in range(m):
    a,b=map(int, input().split())
    if computers.get(a) is None:
        computers[a]=[]
    computers[a].append(b)
    

for i in range(1,n+1):

    bfs(computers,i, n)

k=max(ans)
for i in range(1,n+1):
    if ans[i]==k:
        print(i, end=' ')
# start node가 따로 없음

