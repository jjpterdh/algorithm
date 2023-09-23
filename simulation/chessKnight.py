# 이것이 코딩테스트다


# knight movement
# up down left right
dx=[2, 2, -2, -2, 1, -1, 1, -1]
dy=[1, -1, 1, -1, 2, 2, -2, -2]

graph=[]
for i in range(8):
    num=i+1
    graph.append(['a'+str(num), 'b'+str(num), 'c'+str(num), 'd'+str(num), 'e'+str(num), 'f'+str(num), 'g'+str(num), 'h'+str(num)])

print(graph)


pos=input()
count=0
for i in range(8):
    for j in range(8):
        if graph[i][j]==pos:
            for k in range(8):
                nx=j+dx[k]
                ny=i+dy[k]

                if nx<0 or nx >= 8 or ny <0 or ny >= 8:

                    continue

                count+=1

print(count)

# time: 12분 2초


