# 백준 1940 silver 4

n=int(input())
m=int(input())

num=list(map(int, input().split()))
num.sort()


count=0
start=0
end=len(num)-1
total=0


while True:
    total=num[start]+num[end]
    


    if start>=end:
        break

    if total==m:
        count+=1
        start+=1
        end-=1
    
    elif total>m:
        end-=1
    
    elif total<m:
        start+=1


print(count)