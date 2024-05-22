import sys
input=sys.stdin.readline

n=int(input())

arr=[int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            arr[i], arr[j]=arr[j], arr[i]

for i in arr:
    print(i)