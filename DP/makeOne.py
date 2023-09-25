# 이것이 코딩이다.
x=int(input())
inf=999999

counts=[0]*30001
def makeOne(x, counts):
    # end condition
    if x <1:
        return inf
    
    elif x==1:
        return 0

    if counts[x]!=0:
        return counts[x]
    

    # 나누기 5
    results=[inf]*4
    
    if x%5==0:
        results[0]=makeOne(x//5, counts)+1

    if x%3==0:
        results[1]=makeOne(x//3, counts)+1
    
    if x%2==0:
        results[2]=makeOne(x//2, counts)+1

    results[3]=makeOne(x-1, counts)+1
    
    counts[x]=min(results)
    
    return counts[x]
    

print(makeOne(x, counts))

# time: 12분 26초 

