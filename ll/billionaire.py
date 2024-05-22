def solution(e, starts):
    answer = []
    dp = [0] * (e + 1)
    dp_idx = [0] * (e + 1)

    for i in range(2,e+1):
        for j in range(1,min(e//i+1,i)):
            dp[i*j]+=2
    for i in range(1,int(e**(1/2))+1):
        dp[i**2]+=1



    max_count = 0
    for i in range(e, 0, -1):
        if max_count <= dp[i]:
            max_count = dp[i]
            dp_idx[i] = i
        else:
            dp_idx[i] = dp_idx[i + 1]

    for i in starts:
        answer.append(dp_idx[i])

    print(answer)

    return answer




e=8
starts=[1,3,7]
print(solution(e,starts))



