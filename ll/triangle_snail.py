def solution(n):
    answer = []
    dy=[1,0,-1]
    dx=[0,1,-1]

    tri=[[0 for i in range(0,j+1)]for j in range(0,n+1)]
    tri[1][1]=1
    
    cnt=sum(i for i in range(n+1))
    
    dir=0
    num=2
    y=1
    x=1
    while num<=cnt:
        ny=y+dy[dir]
        nx=x+dx[dir]
        if ny>n or ny <=0 or nx>ny or nx<=0 or tri[ny][nx]!=0:
            dir+=1
            dir%=3
            continue
        
        
        tri[ny][nx]=num
        num+=1
        y=ny
        x=nx
        


    for i in range(1,n+1):
        for j in range(1,i+1):
            answer.append(tri[i][j])


    
        
    return answer



n=8
print(solution(n))