import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
L=[0]*n
L[0]=arr[0]
result=L[0]

for i in range(1, n):
    L[i]=max(arr[i], L[i-1]+arr[i])
    result=max(result, L[i])

R=[0]*n
R[n-1]=arr[n-1]
for i in range(n-2, -1,-1):
    R[i]=max(arr[i], R[i+1]+arr[i])

for i in range(1, n-1):
    temp=L[i-1]+R[i+1]
    result=max(result, temp)

print(result)
