import math
from collections import deque

MAX_NUM=200001
def sol(c,b):
    ans=0
    time=0

    q=deque([])
    visited=[[0]*2 for _ in range(MAX_NUM)]

    q.append([b, time])
    while(1):
        
        
        c+=time
        

        if c>=MAX_NUM:
            ans= -1
            break
        
        if visited[c][time%2]:
            return time
        

        
        for i in range(len(q)):
            cur=q.popleft()
            cur_pos, cur_time=cur[0], cur[1]
            new_time=(cur_time+1)%2

            new_pos=cur_pos-1
            if new_pos>=0 and not visited[new_pos][new_time]:
                 visited[new_pos][new_time]=1
                 q.append([new_pos, new_time])
                
            new_pos=cur_pos+1
            if new_pos<MAX_NUM and not visited[new_pos][new_time]:
                visited[new_pos][new_time]=1
                q.append([new_pos, new_time])
            
            new_pos=cur_pos*2
            if new_pos<MAX_NUM and not visited[new_pos][new_time]:
                visited[new_pos][new_time]=1
                q.append([new_pos, new_time])


        time+=1

    return ans

c,b=map(int, input().split())

ans=sol(c,b)
print(ans)