import sys
from collections import deque
input=sys.stdin.readline

n,m,k,x=map(int,input().split())
graph={}
for i in range(m):
    a,b=map(int, input().split())
    if graph.get(a) is None:
        graph[a]=[]
    graph[a].append(b)



def bfs(start, n,k):
    queue=deque([(start,0)])
    visited=[False]*(n+1)
    visited[start]=True
    answer=[]
    
    while queue:
        node,distance=queue.popleft()
        if graph.get(node) is None:
            continue
        for n in graph[node]:
            
            if not visited[n]:
                visited[n]=True
                queue.append((n,distance+1))
                if distance+1==k:
                    
                    answer.append(n)

    return answer




answer=bfs(x,n,k)
if answer==[]:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)


