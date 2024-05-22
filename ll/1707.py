import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)
k=int(input())
isEven=True
def dfs(start):
    global isEven
    if not isEven:
        return
    visited[start]=True
    for node in graph[start]:
        if not visited[node]:
            check[node]=(check[start]+1)%2
            dfs(node)

        elif check[node]==check[start]:
            isEven=False
            break
    
    

for _ in range(k):
    isEven=True
    
    v,e=map(int, input().split())
    visited=[0]*(v+1)
    check=[0]*(v+1)
    graph=[[] for _ in range(v+1)]
    
    for i in range(e):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    

    for i in range(1,v+1):
        
        if isEven:
            dfs(i)
        else:
            print("NO")
            break

    if isEven:
        print("YES")



# visited 매번 초기화해줘서 성능이 느렸음.
