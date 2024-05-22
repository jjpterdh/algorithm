import heapq as hq
import sys


def dijkstra(start, adj, distance):
    q=[]
    distance[start]=0
    hq.heappush(q, (0, start))

    while q:
        dist, node=hq.heappop(q)
                
        if distance[node] <dist:
            continue

        for next_node in adj[node]:
            next_w=dist+1
            if distance[next_node] > next_w:
                distance[next_node]=next_w
                hq.heappush(q, (next_w, next_node))
        



def solution(n, roads, sources, destination):
    answer = []
    adj=[[]*(n+1)]
    for i in range(len(roads)):
        a,b=roads[i]
        
        adj[a].append(b)
        adj[b].append(a)

    # sources
    distance=[sys.maxsize]*(n+1)
    for s in sources:
        answer.append(dijkstra(s, adj, distance))
    
    return answer

n=5
roads=[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources=[1, 3, 5]
destination=5
print(solution(n, roads, sources, destination))