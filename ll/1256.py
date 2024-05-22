import sys

input=sys.stdin.readline
n,m,k=map(int, input().split())
answer=[]
# aazz
# azaz
dp=[[0]*202 for i in range(202)]

for i in range(0,201):
    for j in range(0,i+1):
        if j==0 or j==i:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            if j > k:
                dp[i][j]= 1000000001

if dp[n+m][m] < k:
    print(-1)

else:
    while not (n==0 and m==0):
        if dp[n-1+m][m]>=k:
            print('a', end='')
            n-=1

        else:
            print('z', end='')
            k-=dp[n-1+m][m]
            m-=1





