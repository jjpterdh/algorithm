from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    
    sum1=sum(queue1)
    sum2=sum(queue2)
    total_len=len(queue1)*3

    if not queue1 or not queue2:
        return -1

    elif sum1==sum2:
        return 0
    
    elif (sum1+sum2)%2!=0:
        return -1
    

    while sum1!=sum2:
        if sum1>sum2:
            num1= queue1.popleft()
            queue2.append(num1)
            sum1-=num1
            sum2+=num1


        else:
            num2= queue2.popleft()
            sum2-=num2
            sum1+=num2
            queue1.append(num2)
    
        
        answer+=1
        if answer>total_len or not queue2 or not queue1:
            answer=-1
            break


    return answer



queue1 = []
queue2 = []
print(solution(queue1, queue2))