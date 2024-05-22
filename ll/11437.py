import sys
from collections import deque
input=sys.stdin.readline
print=sys.stdout.write

n=int(input())
tree=[[]for _ in range(n+1)]
p=[0]*(n+1)
depth=[0]*(n+1)


def LCA(a,b):
    # 깊이 맞추기
    if depth[a]<depth[b]:
        temp=a
        a=b
        b=temp

    while depth[a]!=depth[b]:
        a=p[a]
    
    # 하나씩 위로 올라가기
    while a!=b:        
        a=p[a]
        b=p[b]
        

    return a



for i in range(n-1):
    a,b=map(int,input().split())


    tree[a].append(b)
    tree[b].append(a)


visited=[False]*(n+1)

def BFS(idx):
    queue=deque([1])
    visited[idx]=True
    level=1
    now_size=1
    count=0
    while queue:
        idx=queue.popleft()
        for node in tree[idx]:
            if not visited[node]:
                visited[node]= True
                p[node]=idx
                depth[node]=level
                queue.append(node)
        count+=1
        if count==now_size:
            count=0
            now_size=len(queue)
            level+=1

        
BFS(1)
m=int(input())
ans=[]
for i in range(m):
    a,b=map(int, input().split())
    # ans.append(LCA(a,b))
    print(str(LCA(a,b)))
    print("\n")

# print(ans)