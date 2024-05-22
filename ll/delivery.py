def solution(order):
    answer = 0

    idx=0
    idx2=0
    delievery=1
    stack=[] # 스택 역할
    
    while idx<len(order) and delievery<=len(order):
        
        if order[idx]==delievery: # 만약 순서와 벨트의 택배 번호와 일치하면
            idx+=1
            delievery+=1
            answer+=1

        elif stack and order[idx]==stack[-1]: # 만약 순서와 보조 벨트의 택배 번호와 일치
            while stack:
                if stack[-1]==order[idx]:
                    idx+=1
                    answer+=1
                    stack.pop()
                else:
                    break            
        
        else: # 순서랑 택배 번호가 x일치
            stack.append(delievery)
            delievery+=1
            

    while stack:
        if stack[-1]==order[idx]:
            idx+=1
            answer+=1
            stack.pop()
        else:
            break

    return answer




order=[4, 3, 1, 2, 5]
print(solution(order))