def solution(babbling):
    answer = 0
    baby=["aya", "ye", "woo", "ma"]
    for b in babbling:
        if b in baby:
            answer+=1
    return answer

