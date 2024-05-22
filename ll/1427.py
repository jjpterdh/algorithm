import sys


input=sys.stdin.readline
num=int(input())
arr=[]
while num:
    arr.append(num%10)
    num//=10

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j]>arr[i]:
            arr[i], arr[j]=arr[j], arr[i]

for a in arr:
    print(a, end='')
