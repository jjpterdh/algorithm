def solution(sequence):
    answer = 0
    
    s1=s2=0
    min_s1=0
    min_s2=0
    max_s=-1e9
    pulse=1

    for i in range(len(sequence)):
        s1+=sequence[i]*pulse
        s2+=sequence[i]*(-pulse)

        max_s=max(max_s, s1-min_s1, s2-min_s2)

        min_s1=min(s1, min_s1)
        min_s2=min(s2, min_s2)

        pulse*=-1
    answer=max_s
    return answer

sequence=[2, 3, -6, 1, 3, -1, 2, 4]	
print(solution(sequence))