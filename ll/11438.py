import sys
from collections import deque
input=sys.stdin.readline


n=int(input())


tree=[[0] for _ in range(n+1)]
depth=[0]*(n+1)
visited=[False]*(n+1)

# set Tree
for i in range(n-1):
    a,b=map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

temp=1
kmax=0
while temp<=n:
    temp<<=1
    
    kmax+=1

p=[[0 for j in range(n+1)] for i in range(kmax+1)]


def bfs():
    queue=deque([1])
    visited[1]=True
    level=1
    now_size=1
    count=0

    while queue:
        idx=queue.popleft()

        for node in tree[idx]:
            if not visited[node]:
                visited[node]=True
                p[0][node]=idx
                depth[node]=depth[idx]+1
                queue.append(node)
        count+=1
        if count==now_size:
            count=0
            now_size=len(queue)
            level+=1

bfs()
# set parent
for k in range(1, kmax+1):
    for n in range(1, n+1):
        p[k][n]=p[k-1][p[k-1][n]]

# LCA
def LCA(a,b):

    if depth[a]>depth[b]:
        temp=a
        a=b
        b=temp
        
    for k in range(kmax, -1, -1):
        if pow(2,k) <= depth[b]-depth[a]:
            if depth[a] <= depth[p[k][b]]:
                b=p[k][b]

    for k in range(kmax, -1,-1):
        if a==b:
            break

        if p[k][a] != p[k][b]:
            a=p[k][a]
            b=p[k][b]

    ans=a
    if a!=b:
        ans=p[0][ans]
    
    return ans

m=int(input())


for i in range(m):
    a,b=map(int, input().split())
    print(LCA(a,b))
