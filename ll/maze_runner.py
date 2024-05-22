
dy=[-1,1,0,0]
dx=[0,0,-1,1]


def calc_distance(y1, x1, y2, x2):
    return abs(y1-y2)+abs(x1-x2)




n,m,k=map(int, input().split())
graph=[[0]*(n+1)]
total_move=[0]*(m+1)
for i in range(n):
    graph.append([0]+list(map(int,input().split())))

runners=[[0]]

for i in range(m):
    runners.append(list(map(int,input().split())))
    
out=list(map(int, input().split()))

for i in range(1,m+1):
    y, x=runners[i]
    dis=calc_distance(y, x, out[0], out[1])
    runners[i]=[dis,y, x]


def find_square():
    
    oy,ox=out
    for sz in range(2, n+1):
        for y1 in range(1, n-sz+2):
            for x1 in range(1,n-sz+2):
                x2, y2 = x1 + sz - 1, y1 + sz - 1

                # 만약 출구가 해당 정사각형 안에 없다면 스킵합니다.
                if not (x1 <= ox and ox <= x2 and y1 <= oy and oy <= y2):
                    continue
                    
            
                # 한 명 이상의 참가자가 해당 정사각형 안에 있는지 판단합니다.
                is_traveler_in = False
                for l in range(1, m + 1):
                    _, ry, rx = runners[l]
                    if x1 <= rx and rx <= x2 and y1 <= ry and ry <= y2:
                        # 출구에 있는 참가자는 제외합니다.
                        
                        if not (rx == ox and ry == oy):
                            is_traveler_in = True
                            
            
                if is_traveler_in:
                    return (y1, x1, sz)

    return (0,0,0)


def rotate(graph): # 90도 방향
    
    
    # 좌상단 반환
    y, x,w=find_square()
    if y==0:
        return(0,0,0)
    # print(y, x, w)
    
    
    
    new_graph=[[0 for _ in range(n+1)] for p in range(n+1)]
    out_y, out_x=out[0],out[1]


    for i in range(y, y+w):
        for j in range(x,x+w):
            
            oy,ox=i-y, j-x
            ry, rx=ox, w-oy-1
            
            # 출구 계산
            if i==out_y and j==out_x:
                out[0]=ry+y
                out[1]=rx+x
                
            
            
            # # runner
            # for l in range(1,m+1):
            #     dis, runner_y, runner_x=runners[l]
            #     if dis==0:
            #         continue
            #     if runner_y==i and runner_x==j:
            #         runners[l]=[dis, ry+y, rx+x]


            # graph            
            new_graph[ry+y][rx+x]=graph[i][j]
            
    
    
    for i in range(y, y+w):
        for j in range(x,x+w):
            
            graph[i][j]=new_graph[i][j]

            # 벽 내구도 감소
            if graph[i][j]>0:
                graph[i][j]-=1


    return (y, x, w)
        # graph=new_graph

def rotate_runners(y1, x1, w):
    y2=y1+w-1
    x2=x1+w-1

    for l in range(1,m+1):
        dis, ry, rx=runners[l]
        if dis==0:
            continue

        if y1<=ry and ry<=y2 and x1<=rx and rx<=x2:
            oy, ox=ry-y1, rx-x1
            ny, nx=ox, w-oy-1

            runners[l]=[dis, ny+y1, nx+x1]



def move(idx):
    dis,y,x=runners[idx]
    
    for i in range(4):
        ny=dy[i]+y
        nx=dx[i]+x

        if ny<=0 or ny>n or nx<=0 or nx>n: # out of boundary
            continue

        if graph[ny][nx]!=0: # 벽 
            continue
        
        new_dis=calc_distance(ny, nx, out[0], out[1])

        if new_dis<dis: # 상 하로 먼저 움직임. 
            if new_dis==0:
                
                runners[idx]=[0,0,0]
                total_move[idx]+=1

            else:
                
                # runner 리스트 갱신
                dis=new_dis
                y=ny
                x=nx
                runners[idx]=[dis, y, x]
                total_move[idx]+=1
            break
        


for time in range(1,k+1):
    
    # print("time:", time)
    # 이동
    count=0
    for i in range(1,m+1):
        if runners[i][0]!=0: # 탈출하지 못한 러너
            move(i)
        else:
            count+=1



    
    # 모두 탈출했는지 확인
    if count==m:
        break

    # 회전
    y1, x1, w=rotate(graph)
    if y1==0:
        break
    rotate_runners(y1, x1, w)
    # print("out:", out)
    # print(runners[1:])
    
    
    
    for i in range(1,m+1):
        dis, y, x=runners[i]
        if dis==0:
            continue
        new_ids=calc_distance(y, x, out[0], out[1])
        runners[i]=[new_ids, y, x]
    



print(sum(total_move))
print(out[0], out[1])