import sys

input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))


sorted_arr=sorted(arr)

total=0
for i in range(n):
    if i-1>=0:
        sorted_arr[i]+=sorted_arr[i-1]
    total+=sorted_arr[i]


print(total)