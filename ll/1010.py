import sys

input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n,m=map(int, input().split())

    d=[0]*(m+1)
    d[0]=1
    for i in range(1,m+1):
        d[i]=d[i-1]*i

    print(d[m]//(d[m-n]*d[n]))