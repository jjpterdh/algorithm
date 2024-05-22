import sys

input=sys.stdin.readline

def fibo(num):
    for i in range(2,num+1):
        dp[i]=dp[i-1]+dp[i-2]
    return 


n=int(input())
dp=[0]*(n+1)
dp[1]=1
fibo(n)
print(dp[n])