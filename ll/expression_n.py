def solution(N, number):
    answer = -1
    if number==1:
        return 1
    
    dp=[]
    for cnt in range(1,9):
        partial_set=set()
        partial_set.add(int(str(N)*cnt))
        for i in range(cnt-1):
            print(dp)
            for op1 in dp[i]:
                for op2 in dp[-i-1]:
                    
                    print(op1, op2)
                    partial_set.add(op1*op2)
                    partial_set.add(op1+op2)
                    partial_set.add(op1-op2)
                    if op2!=0:
                        partial_set.add(op1//op2)
            

        if number in partial_set:
            return cnt
        dp.append(partial_set)
        
                    

    return answer


N=5
number=12
print(solution(N, number))

# https://alreadyusedadress.tistory.com/115