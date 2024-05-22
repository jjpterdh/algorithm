import sys

sys.setrecursionlimit(10**6)
input=sys.stdin.readline


n,m=map(int,input().split())
textList=set([input() for _ in range(n)])
count=0
for _ in range(m):
    text=input()
    if text in textList:
        count+=1

print(count)