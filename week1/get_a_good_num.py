# 백준 1253번

n=int(input())
num=list(map(int, input().split()))
num.sort()


start=0
end=n-1
i=0
count=0
while True:

    total=num[start]+num[end]
    if i>=n:
        break


    if start>=end:
        i+=1
        start=0
        end=n-1
    
    elif total > num[i]:
        end-=1
    
    elif total < num[i]:
        start+=1

    else:
        if start!=i and end!=i:
        
            i+=1
            count+=1
            start=0
            end=n-1
        
        elif start==i:
            start+=1
        
        elif end==i:
            end-=1

print(count)


