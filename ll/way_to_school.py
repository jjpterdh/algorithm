
mod=1000000007

def solution(m, n, puddles):
    answer = 0
    
    graph=[[0 for i in range(m+1)]for j in range(n+1)]
    dp=[[0]*(m+1) for _ in range(n+1)]
    dp[1][1]=1
    graph[1][1]=1
    graph[n][m]=3
    for x, y in puddles:
        graph[y][x]=2

    for i in range(1,n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if graph[i][j]==2: # 웅덩이
                continue

            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod
    answer=dp[n][m]

    
    
    return answer

puddles=[[2, 2]]
print(solution(4,3,[[2, 2]]))