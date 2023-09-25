# 깊이 우선 탐색
INF=999999999

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end='')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)






graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

print(graph[2])
# 1~8번 노드까지 있으므로 0~8번 노드 방문을 false로 만듦
visited=[False]*9


# dfs(graph,1, visited)
# print(visited)