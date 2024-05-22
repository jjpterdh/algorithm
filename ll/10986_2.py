import sys
input=sys.stdin.readline

n,m=map(int, input().split())

arr=[0]+list(map(int, input().split()))

sum_arr=[0]*(n+1)
for i in range(1,n+1):
    sum_arr[i]=((arr[i]%m)+(sum_arr[i-1]%m))%m

count=0
poss=[0]*(m)
for i in range(1,n+1):
    if sum_arr[i]==0:
        count+=1

    poss[sum_arr[i]]+=1
    
# 경우의 수 사용
for i in range(m):
    if poss[i]>1:
        count+=(poss[i]*(poss[i]-1))//2
        

    

print(count)