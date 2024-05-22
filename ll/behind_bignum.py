def solution(numbers):
    
    stack=[]
    ans=[0]*(len(numbers))

    for i in range(len(numbers)):
        if not stack:
            stack.append(i)
        else:
            
            if numbers[stack[-1]]<numbers[i]:
                while stack and numbers[stack[-1]]<numbers[i]:
                    
                    ans[stack[-1]]=numbers[i]
                    stack.pop()
                   
            
            stack.append(i)
    
    for i in range(len(ans)):
        if ans[i]==0:
            ans[i]=-1


    return ans



numbers=[2, 3, 3, 5]
print(solution(numbers))