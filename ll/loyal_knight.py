from collections import deque
import sys

# sys.setrecursionlimit(10**6)
dy=[-1,0,1,0]
dx=[0,1,0,-1]


l,n,q=map(int, input().split()) # 체스판, 기사의 수, 명령의 수
knights=[0]*(n+1)
knights_pos=[[0,0] for i in range(n+1)]
graph=[[0]*(l+1)]
for _ in range(l):
    graph.append([0]+list(map(int, input().split())))  # 0: 빈칸, 1: 함정, 2: 벽
graph_knight=[[0 for i in range(l+1)] for _ in range(l+1)] 

move_check=[False]*(n+1)
moved_list=[False]*(n+1)


for idx in range(1, n+1):
    r,c ,h,w,k=map(int, input().split())
    knights[idx]=k
    knights_pos[idx]=[r,c,h,w]
    for i in range(r, r+h):
        for j in range(c, c+w):
            graph_knight[i][j]=idx

# print(knights)
def del_knight(idx):
    y,x,h,w=knights_pos[idx]
    for i in range(y,y+h):
        for j in range(x, x+w):
            graph_knight[i][j]=0

def update_point(idx,n): # 포인트 집계

    global damage
    for i in range(1,n+1):
        count=0
        if i==idx: # 본인일때 x 감점
            continue
        elif not move_check[i]: # 움직이지 않았을 때 
            continue

        y,x,h,w=knights_pos[i]
        for j in range(y,y+h):
            for k in range(x, x+w):
                if graph[j][k]==1:
                    count+=1
        
        if knights[i]>count:
            damage[i]+=count
            knights[i]-=count
            
        else:
            damage[i]=0
            knights[i]=0
            del_knight(i)
        

    # return damage

def dfs(y,x,h,w,di): # 연쇄 움직임
    global move_check
    global moved_list
    # di 방향으로 연쇄 기사 탐색
    moved=True # 위에 벽이나 밖이나 다른 기사가 없음.
    
    
    # 상
    if di==0:
        for i in range(x, x+w):
            ny=y+dy[di]
            nx=i+dx[di]

            # 맵 밖으로
            if ny<=0 or ny>l or nx<=0 or nx>l:
                moved=False
                break
            # 벽
            elif graph[ny][nx]==2 or not moved:
                moved=False
                break
            
            # 다른 기사가 존재
            elif graph_knight[ny][nx]!=0:
                nidx=graph_knight[ny][nx]
                moved_list[nidx]=True
                ky,kx,kh,kw=knights_pos[nidx]
                # 다른 기사 탐색 + 움직였으면 움직이기
                moved=dfs(ky, kx, kh,kw, di)
        
                
    # 우
    elif di==1:
        x+=w-1
        for i in range(y, y+h):
            ny=i+dy[di]
            nx=x+dx[di]
            # 맵 밖으로
            if ny<=0 or ny>l or nx<=0 or nx>l:
                moved=False
                break
            # 벽
            elif graph[ny][nx]==2 or not moved:
                moved=False
                break

            # 다른 기사가 존재
            elif graph_knight[ny][nx]!=0:
                nidx=graph_knight[ny][nx]
                moved_list[nidx]=True
                ky,kx,kh,kw=knights_pos[nidx]
                # 다른 기사 탐색 + 움직였으면 움직이기
                moved=dfs(ky, kx, kh,kw, di)

    
    # 하
    elif di==2:
        y+=h-1
        for i in range(x, x+w):
            ny=y+dy[di]
            nx=i+dx[di]
            # 맵 밖으로
            if ny<=0 or ny>l or nx<=0 or nx>l:
                moved=False
                break
            # 벽
            elif graph[ny][nx]==2 or not moved:
                moved=False
                break
            
            # 다른 기사가 존재
            elif graph_knight[ny][nx]!=0:
                nidx=graph_knight[ny][nx]
                moved_list[nidx]=True
                ky,kx,kh,kw=knights_pos[nidx]
                
                # 다른 기사 탐색 + 움직였으면 움직이기
                moved=dfs(ky, kx, kh,kw, di)

    # 좌
    else:
        for i in range(y,y+h):
            ny=i+dy[di]
            nx=x+dx[di]

            # 맵 밖으로
            if ny<=0 or ny>l or nx<=0 or nx>l:
                moved=False
                break
            # 벽
            elif graph[ny][nx]==2 or not moved:
                moved=False
                break

            # 다른 기사가 존재
            elif graph_knight[ny][nx]!=0:
                nidx=graph_knight[ny][nx]
                moved_list[nidx]=True
                ky,kx,kh,kw=knights_pos[nidx]
                
                # 다른 기사 탐색 + 움직였으면 움직이기
                moved=dfs(ky, kx, kh,kw, di)
                
    

    if moved:
        move_check[graph_knight[y][x]]=True
        # move(graph_knight[y][x], di)
        

    return moved


def move(idx, di): # 기사 움직임
    y,x,h,w=knights_pos[idx]


    # 기존 나이트 위치 지우기
    for i in range(y,y+h):
        for j in range(x,x+w):
            if graph_knight[i][j]==idx:
                graph_knight[i][j]=0

    y+=dy[di]
    x+=dx[di]
    # 기사 위치 리스트 업데이트
    knights_pos[idx]=[y,x,h,w]
    
    for i in range(y,y+h):
        for j in range(x,x+w):
            graph_knight[i][j]=idx




damage=[0]*(n+1)
for _ in range(q):
    
    idx, di=map(int, input().split())
    moved_list[idx]=True
    # 체스판에서 사라진 기사
    if knights[idx]<=0:
        continue

    y,x,h,w=knights_pos[idx]
    

    dfs(y,x,h,w,di) 
        
    

    flag=True
    for i in range(1,n+1):
        if move_check[i]!=moved_list[i]:
            flag=False
            break

    if flag:
        for i in range(1,n+1):
            if move_check[i]==True:
                move(i, di)


        update_point(idx, n)


    #########################
    # print("======== round", _,"===========")
    # for i in range(1,l+1):
    #     for j in range(1, l+1):
    #         if graph[i][j]==2:
    #             print("-", end=' ')
    #         else:
    #             print(graph_knight[i][j], end=' ')

    #     print()
    # print()


    # print(moved_list)
    # print(move_check)
###################################
    move_check=[False]*(n+1)
    moved_list=[False]*(n+1)
    # if max_num==0:
    #     break
# print(knights)
print(sum(damage))
# 상 우 하 좌
# 0 1 2 3