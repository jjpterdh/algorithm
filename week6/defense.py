def backtracking(n, k, pos, enemy, answer):
    if k==0:
        for i in range(len(enemy)):
            if n < enemy[i]:
                break
            answer=max(i, answer)
            n-=enemy[i]
        return answer
    
    else:
        for i in range(pos, len(enemy)):
            tmp_enemy=enemy[:]
            tmp_enemy[pos]=0
            
            answer=max(answer, backtracking(n, k-1, i+1, tmp_enemy, answer))

        return answer
            

def solution(n, k, enemy):
    answer=0
    for i in range(len(enemy)):
        answer=max(answer, backtracking(n, k, i, enemy, 0))
    
    answer+=1
    
    return answer

n=7
k=3
enemy=[4,2,4,5,3,3,1]
print(solution(n, k, enemy))