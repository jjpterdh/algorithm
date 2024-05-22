import sys

input=sys.stdin.readline
n=int(input())
scores=list(map(int, input().split()))

max_score=max(scores)
m=100/max_score
total=sum(scores)
total*=m
total/=n
print(total)

