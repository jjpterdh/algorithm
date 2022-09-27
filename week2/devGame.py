# n*m 맵
# 육지: 0/바다: 1
# 동서남북 방향 
# 맵 (a,b) a= 북으로부터 떨어진 칸의 개수, b는 서쪽으로부터 떨어진 칸의 개수
dirs=[0, 3, 2, 1] # 북 서 남 동
dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]

n,m=map(int, input().split())
x,y, dir=map(int, input().split())
table=[]

for i in range(n):
    table.append(list(map(int, input().split())))




count=0
while True:
    dir=(1+dir)%4
    
    #check is this ocean
    if table[y][x]==1 and flag==4:
        break

    # 주위에 빈칸이 있는지 확인
    flag=0
    for i in range(4):
        visit_x=x+dx[i]
        visit_y=y+dy[i]
        if visit_x<0 or visit_y<0 or table[visit_y][visit_x]==1:
            flag+=1


    # 방향 전환및 이동
    tmpx=x
    tmpy=y
    if flag<4:
        for j in range(3):
            tmpx+=dx[dir]
            tmpy+=dy[dir]
            if tmpx>=0 and tmpy>=0:
                if table[tmpy][tmpx]==0: # 비어있는 칸
                    print("x: ", tmpx, " y:", tmpy)
                    table[tmpy][tmpx]=1
                    count+=1
                    x=tmpx
                    y=tmpy
                    break
                else: # 이미 방문/ 바다인 경우 방향 돌리기
                    dir=(1+dir)%4

            else:
                dir=(1+dir)%4

    else:
        #뒤로 한칸 이동 
        x=x-dx[dir]
        y=y-dy[dir]

print(count+1)