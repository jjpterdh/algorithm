from collections import deque
import sys
def bfs(roads_info, start, n, graph):
    visited=[False]*(n+1)
    
    graph[start]=0
    visited[start]=True
    queue=deque([start])
    while queue:
        cur_node=queue.popleft()
        
        if roads_info.get(cur_node) is None:
            continue
        
        for new_node in roads_info[cur_node]:
            if not visited[new_node]:
                visited[new_node]=True
                queue.append(new_node)
                

            if graph[cur_node]+1 < graph[new_node]:
                graph[new_node]=graph[cur_node]+1
            
                queue.append(new_node)

    


def solution(n, roads, sources, destination):
    answer = []
    roads_info={}
    for i in range(len(roads)):
        a,b=roads[i]
        if roads_info.get(a) is None:
            roads_info[a]=[]
        if roads_info.get(b) is None:
            roads_info[b]=[]

        roads_info[a].append(b)
        roads_info[b].append(a)

    # sources
    graph=[sys.maxsize]*(n+1)
    bfs(roads_info, destination, n, graph)
    
    for s in sources:
        if graph[s]==sys.maxsize:
            answer.append(-1)
        else:
            answer.append(graph[s])
        
    
    return answer


n=5
roads=[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources=[1, 3, 5]
destination=5
print(solution(n, roads, sources, destination))