import sys
input=sys.stdin.readline
inf=1e9
ddr=list(map(int, input().split()))
dp=[[[inf for _ in range(5)] for k in range(5)] for i in range(100001)]
dp[0][0][0]=0
L=0
R=0
mp=[[0,2,2,2,2],
    [2,1,3,4,3],
    [2,3,1,3,4],
    [2,4,3,1,3],
    [2,3,4,3,1]]
s=1

idx=0
while ddr[idx]!=0:
    next_num=ddr[idx]
    for i in range(5):
        if next_num==i:
            continue
        for j in range(5):
            dp[s][i][next_num]=min(dp[s-1][i][j]+mp[j][next_num],dp[s][i][next_num])

    for j in range(5):
        if next_num==j:
            continue
        for i in range(5):
            dp[s][next_num][j]=min(dp[s-1][i][j]+mp[i][next_num], dp[s][next_num][j])

    s+=1
    idx+=1

s-=1
result=inf
for i in range(5):
    for j in range(5):
        result=min(result, dp[s][i][j])

print(result)