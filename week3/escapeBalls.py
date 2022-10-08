# 삼성 기출
# 공 탈출2
from collections import deque

n, m = map(int, input().split())

graph=[]
visited=[]

for i in range(n):
    graph.append(list(input()))
    visited.append( list(False for i in range(m)))
    if 'R' in graph[i]:
        rx= graph[i].index('R')
        ry= i

    if 'B' in graph[i]:
        bx= graph[i].index('B')
        by= i    



# 기울기 영향 받는 물체: R, B
dx= [1, -1, 0, 0]
dy= [0, 0, 1, -1]



def bfs(ry, rx, by, bx):
    #terminate condition 
    # red ball -> O
    # red ball cannot get out
    # reb ball & blue ball -> O (-1)
    
    #red ball
    queue_r=deque()
    count=1
    queue_r.append([ry, rx, count])
    

    # blue ball
    queue_b=deque()
    queue_b.append([by, bx])

    


    while queue_r:
        # red ball
        pos_r=queue_r.popleft()
        ry= pos_r[0]
        rx= pos_r[1]
        count=pos_r[2]
        
        # blue ball
        pos_b=queue_b.popleft()
        by=pos_b[0]
        bx=pos_b[0]

        

        
        for i in range(4): # right, left, down, up
            tmp_rx=rx
            tmp_ry=ry
            
            tmp_bx=bx
            tmp_by=by
            tmp_count=count
            while tmp_rx+dx[i] >=0 and tmp_rx+dx[i] <m and tmp_ry+dy[i] >=0 and tmp_ry+dy[i] <n: # 기울어진 방향으로 끝까지 이동
                
                
                
                if graph[tmp_ry+dy[i]][tmp_rx+dx[i]]=='.' or graph[tmp_ry+dy[i]][tmp_rx+dx[i]]=='O' :
                    
                    if graph[tmp_ry+dy[i]][tmp_rx+dx[i]]=='O':
                        graph[tmp_by+dy[i]][tmp_rx+dx[i]]='.'
                        return count
                    
                    if not visited[tmp_ry+dy[i]][tmp_rx+dx[i]]:
                        visited[tmp_ry+dy[i]][tmp_rx+dx[i]]=True
                        tmp_rx=tmp_rx+dx[i]
                        tmp_ry=tmp_ry+dy[i]

                    else:
                        break
                    
                
                else: # 빨간공이 끝까지 도착해도 파란공이 끝까지 도착안한 케이스
                    break
            
            if tmp_rx!=rx or tmp_ry!=ry: # different from original value
                # count+=1
                tmp_count+=1
                queue_r.append([tmp_ry, tmp_rx, tmp_count])

            
            while tmp_bx+dx[i] >=0 and tmp_bx+dx[i] <m and tmp_by+dy[i] >=0 and tmp_by+dy[i] <n:                        
                if graph[tmp_by+dy[i]][tmp_bx+dx[i]]=='.' or graph[tmp_by+dy[i]][tmp_bx+dx[i]]=='O':
                    if graph[tmp_by+dy[i]][tmp_bx+dx[i]]=='O': #blue ball이 구멍에 들어갈 경우
                        return -1


                    tmp_bx=tmp_bx+dx[i]
                    tmp_by=tmp_by+dy[i]
                else:
                    break

            if tmp_bx!=bx or tmp_by!=by: # different from original value
                queue_b.append([tmp_by, tmp_bx])
                
            


                
                
            
        
            


    return -1

##############################################################################


print(bfs(ry, rx, by, bx))
