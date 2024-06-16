# 백준 #11659
import sys
input=sys.stdin.readline
n,m=map(int, input().split())

arr=list(map(int, input().split()))
sum_arr=[]
total=0
for i in range(n):
    total+=arr[i]
    sum_arr.append(total)


for k in range(m):
    i,j=map(int, input().split())
    i-=1

    if i!=0:

        total=sum_arr[j-1]-sum_arr[i-1]
    else:
        total=sum_arr[j-1]
    
    print(total)
