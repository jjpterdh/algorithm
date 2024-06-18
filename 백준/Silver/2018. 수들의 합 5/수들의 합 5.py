# 2018 백준 연속된 자연수의 합 구하기

n=int(input())


count=1
start=1
end=1
sum=0

while True:
    
    if start==n:
        break

    elif sum==n:
        sum+=end
        end+=1        
        count+=1

    elif sum>n:
        sum-=start
        start+=1
        

    elif sum<n:
        sum+=end
        end+=1


print(count)