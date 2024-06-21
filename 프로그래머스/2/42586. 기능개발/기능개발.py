
def solution(progresses, speeds):
    answer = []
    days=[]
    stack=[]
    for i in range(len(progresses)):
        
        remain=100-progresses[i]
    
        if remain%speeds[i]!=0:
            days.append(remain//speeds[i]+1)
        else:
            days.append(remain//speeds[i])
    # print(days)

    for d in range(len(days)):
        count=0          
        if stack and stack[0]<days[d]:
            count=len(stack)
            stack=[]
            answer.append(count)

        stack.append(days[d])

    count=len(stack)
    answer.append(count)
        

    return answer