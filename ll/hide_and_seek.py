

dy=[-1,0,1,0]
dx=[0,1,0,-1]

n,m,h,k=map(int, input().split())
runners=[[]]
trees=[]

for i in range(m):
    y,x,d=map(int, input().split())
    dir=0
    if d==1: # 좌우
        dir=1
    else: # 상하
        dir=2

    runners.append([y,x,dir])

for i in range(h):
    trees.append(list(map(int, input().split())))

def cal_dis():
    # 3 이하인 도망자만 움직임
    return 


# 도망자 -> 술래 움직임

def runner_move():

    #

    # 보드 안
    # 1. 술래없을 때
    # 2. 나무는 ㄱㅊ
    
    # 보드 밖
    # 1. 방향 반대로
    # 2. 반대로 돌았을때 술래가 없으면 움직임


    return

def catcher_move(reverse):

    # 순방향

    # 역방향


    # 움직임 이후 3칸 확인

    return


# 도망자 
# 좌우 (오른쪽)
# 상하 (아래쪽)


for _ in range(k):
    runner_move()
    catcher_move()