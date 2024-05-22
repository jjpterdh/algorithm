import sys

input=sys.stdin.readline

mod=1000000007

n,l,r=map(int, input().split())
d=[[[0 for i in range(101)]for j in range(101)] for k in range(101)]
d[1][1][1]=1

for i in range(2,n+1):
    for j in range(1,l+1):
        for k in range(1, r+1):
            d[i][j][k]=((d[i-1][j-1][k]+d[i-1][j][k-1])+d[i-1][j][k]*(i-2))%mod


print(d[n][l][r])