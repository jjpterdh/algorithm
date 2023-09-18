def solution(n, k, enemy):

    answer=0

    if len(enemy) < k:
        return len(enemy)    

    max_num = []
    for i in range(len(enemy)):
        if n < enemy[i] and k > 0: # n이 작고 무적권이 남아 있을 때
            max_num.append(enemy[i])
            max_num.sort(reverse=True)
            k-=1
            n+=max_num.pop(0)
            answer=i
            
            if n < enemy[i]:                
                break
            else:
                n-=enemy[i]

        elif n < enemy[i]: # n이 작고 무적권이 없을 때                        
            break

        else:
            max_num.append(enemy[i])
            max_num.sort(reverse=True)            
            answer=i
            n-=enemy[i]
            
            
    return answer+1

    # n=2
    # k=4
    # enemy=[3,3,3,3]
    # print(solution(n, k, enemy))

    # n=7
    # k=3
    # enemy=[4,2,4,5,3,3,1]   
    # print(solution(n, k, enemy))