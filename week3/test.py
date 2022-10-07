from collections import deque
# graph = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]

# for i in range(4):
#     for j in range(5):

#         print(graph[i][j], end='')
#     print()

queue=deque()

queue.append([1,1])
pos=queue.popleft()
print(pos)
