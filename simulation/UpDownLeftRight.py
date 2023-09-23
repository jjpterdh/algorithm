# 이것이 코딩테스트다


n=int(input())
moves=list(input().split())

def solution(n, moves):
    x,y=0,0
    for i in range(len(moves)):
        if moves[i]=='L':
            dx=-1
            dy=0

        elif moves[i]=='R':
            dx=1
            dy=0

        elif moves[i]=='U':
            dx=0
            dy=-1

        else:
            dx=0
            dy=1

        nx=x+dx
        ny=y+dy

        if nx < 0 or nx >=n or ny<0 or ny >=n:
            continue

        x=nx
        y=ny

    return y+1,x+1
print(solution(n,moves))

# 소요시간: 8분 24초