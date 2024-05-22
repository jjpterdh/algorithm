import sys

input=sys.stdin.readline
n,d,k,c=map(int, input().split())

sushi=[]
for i in range(n):
    sushi.append(int(input()))

sushi*=2
count=0
for i in range(n):
    types=set(sushi[i:i+k])
    if c not in types:
        count=max(count, len(types)+1)
    else:
        count=max(count, len(types))

print(count)
