def solution(triangle):
    answer = 0


    dp=[[0 for _ in range(len(triangle))]for i in range(len(triangle))]
    for i in range(len(triangle)):
        dp[len(triangle)-1][i]=triangle[len(triangle)-1][i]
    
    for i in range(len(triangle)-2, -1 ,-1):
        for j in range(i+1):
            dp[i][j]=max(triangle[i][j]+dp[i+1][j], triangle[i][j]+dp[i+1][j+1])
    
    answer=dp[0][0]
    return answer

triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))