import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
arr=list(map(int, input().split()))

arr.sort()
cnt=0
start=0
end=len(arr)-1

while start<end:
    s=arr[start]+arr[end]
    if s==m:
        cnt+=1
        start+=1

    elif s>m:
        end-=1

    else:
        start+=1

print(cnt)
