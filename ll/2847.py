import sys

input=sys.stdin.readline
n=int(input())

scores=[]
for i in range(n):
    scores.append(int(input()))

total=0
for i in range(n-2, -1, -1):
    if scores[i+1]<=scores[i]:
        total+=(scores[i]-(scores[i+1]-1))
        scores[i]=scores[i+1]-1

print(total)