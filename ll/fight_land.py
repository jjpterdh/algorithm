# 의문점: 진 플레이어는 바로 이동하는지?
# 아니면 순서대로 이동하는지

dy=[-1, 0, 1, 0]
dx=[0,1,0,-1]

n,m,k=map(int, input().split())

board=[[0]*(n+1) for _ in range(n+1)]
players=[[]]
points=[0]*(m+1)


for i in range(1,n+1):
    guns=list(map(int, input().split()))
    for j in range(1,n+1):
        board[i][j]=[]
        board[i][j].append(guns[j-1])


for i in range(m):
    players.append(list(map(int, input().split()))+[0]) # y, x, dir, s, gun

def fight(a,b):
    _,_,_,s1, g1=players[a]
    power1=s1+g1
    _,_,_,s2, g2=players[b]
    power2=s2+g2
    loser=a
    winner=b
    if power1==power2:
        if s1>s2: 
    
            loser=b
            winner=a
            points[a]+=0

        else: # s2>s1
            
            loser=a
            winner=b
            points[b]+=0


    elif power1>power2:
        loser=b
        winner=a
        points[a]+=(power1-power2)

    else:
        points[b]+=(power2-power1)
        loser=a
        winner=b

    return (winner,loser)

def move(idx):
    # 진 사람 무브 따로 짜기
    y,x,d,s,g=players[idx]

    ny=y+dy[d]
    nx=x+dx[d]
    winner, loser=idx,0
    # out of boundary 방향 바꾸기.
    if ny<=0 or ny>n or nx<=0 or nx>n:
        d+=2
        d%=4
        ny=y+dy[d]
        nx=x+dx[d]
    
    # 사람 만났을 때
    for idx2 in range(1, m+1):
        y2,x2,d2,s2,g2=players[idx2]

        if ny==y2 and nx==x2:
            winner, loser=fight(idx, idx2)
            
            ly, lx, ld, ls, lg=players[loser]
            wy, wx, wd, ws, wg=players[winner]
            players[winner]=[ny,nx, wd,ws,wg]
            # 진 사람은 총을 내려놓기
            board[ny][nx].append(lg)
            lg=0
            if idx==loser:
                ld=d
            players[loser]=[ny,nx,ld,ls,lg]
            
            loser_move(loser)
            break

    # 이긴사람 총 비교
    wy, wx, wd, ws, wg=players[winner]
    if idx==winner:
        wd=d
    if board[ny][nx]!=[0]:
        for gidx in range(len(board[ny][nx])):
            new_gun=board[ny][nx][gidx]
            
            # 총비교
            if wg<new_gun:
                # 총 내려놓고 바꾸기
                tmp=wg
                wg=new_gun
                board[ny][nx][gidx]=tmp

    players[winner]=[ny,nx, wd,ws,wg]
    

def loser_move(idx):
    
    y,x,d,s,g=players[idx]
    ny=0
    nx=0
    while True:
        
        flag=True
        ny=y+dy[d]
        nx=x+dx[d]
        
        # 벽일 경우
        if ny<=0 or ny>n or nx<=0 or nx>n:
            
            d+=1
            d%=4
            flag=False
            
        
        # 사람이 있을 경우
        for idx2 in range(1, m+1):
            y2,x2,_,_,_=players[idx2]
            if ny==y2 and nx==x2:
                
                d+=1
                d%=4
                flag=False
                break
        
        # 
        if flag:
            break
    
    # 총 비교
    if board[ny][nx]!=[0]:
        for gidx in range(len(board[ny][nx])):
            new_gun=board[ny][nx][gidx]
        
            if g<new_gun:
                # 총 내려놓고 바꾸기
                tmp=g
                g=new_gun
                board[ny][nx][gidx]=tmp

    players[idx]=[ny,nx,d,s,g]

for _ in range(k):

    for i in range(1,m+1):    
        move(i)

    # print('round:', _+1)
    # for i in range(1,n+1):
    #     for j in range(1, n+1):
    #         print(board[i][j], end=' ')
    #     print()
    # print()
    # print(players[1:])
    

# output
for i in range(1,m+1):
    print(points[i], end=' ')




