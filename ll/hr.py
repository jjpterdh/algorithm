
def solution(scores):
    answer = 0
    won_a,won_b=scores[0][0], scores[0][1]
    won=won_a+won_b

    
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb=0

    for i in range(len(scores)):
        a=scores[i][0]
        b=scores[i][1]

        if a>won_a and b>won_b:
            return -1
        if b>=maxb:
            maxb=b
            if a+b>won:
                answer+=1


    return answer+1

scores=[[2,2],[1,4],[3,2],[3,2],[2,1], [1,2]]
print(solution(scores))