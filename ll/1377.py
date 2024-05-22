import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    arr.append((int(input()), i))


Max=0
sorted_arr=sorted(arr)

for i in range(n):
    if Max<sorted_arr[i][1]-i:
        Max=sorted_arr[i][1]-i


print(Max+1)