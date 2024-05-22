def check_graph(graph):
    donut=0
    stick=0
    eight=0
    key=0
    for node, edges in graph.items():
        if edges[0]>=2 and edges[1]==0:
            key=node
        elif edges[0]==0 and edges[1]>=1:
            stick+=1
        elif edges[0]>=2 and edges[1]>=2:
            eight+=1
    donut=graph[key][0]-stick-eight

    
    
    return [key, donut, stick, eight]

def solution(edges):
    graph={}
    
    for edge in edges:
        if graph.get(edge[0]) is None:
            graph[edge[0]]=[0,0]
        if graph.get(edge[1]) is None:
            graph[edge[1]]=[0,0]

        # 0은 나가는 간선
        graph[edge[0]][0]+=1
        # 1은 들어오는 간선
        graph[edge[1]][1]+=1

    
    answer=check_graph(graph)


    

    return answer


edge=[[2, 3], [4, 3], [1, 1], [2, 1]]
edge2=[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
print(solution(edge2))