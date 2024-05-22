def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[1])
    print(targets)
    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer 


targets=[[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	
print(solution(targets))
