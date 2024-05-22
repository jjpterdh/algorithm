inf=1e9

def solution(x, y, n):
    if x==y:
        return 0
    
    answer = 0
    d=[inf]*(y+1)
    d[x]=0
    for i in range(x,y+1):
        if d[i]==inf:
            continue
        if i+n<=y:

            d[i+n]=min(d[i+n],d[i]+1)

        if i*2<=y:
            d[i*2]=min(d[i*2], d[i]+1)

        if i*3<=y:
            d[i*3]=min(d[i*3], d[i]+1)

    answer=d[y]
    
    if answer==inf:
        return -1
    return answer

    
    
    




print(solution(10, 40, 5))