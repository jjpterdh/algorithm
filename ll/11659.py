import sys
input= sys.stdin.readline
n,m=map(int, input().split())

arr=list(map(int, input().split()))

sum_arr=list()
sum_arr.append(0)
sum=0
for i in range(1,len(arr)+1):
    sum+=arr[i-1]
    sum_arr.append(sum)

for k in range(m):
    i,j=map(int, input().split())

    ans=sum_arr[j]-sum_arr[i-1]
    print(ans)

    