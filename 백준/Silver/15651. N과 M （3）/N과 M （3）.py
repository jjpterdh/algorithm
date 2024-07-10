import sys

input=sys.stdin.readline

n,m=map(int, input().split())
arr=[]

def dfs(cnt):
    if cnt==m:
        print(' '.join(map(str, arr)))
    else:
        for i in range(1,n+1):
            arr.append(i)
            dfs(cnt+1)
            arr.pop()


dfs(0)