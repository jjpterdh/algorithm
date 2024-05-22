
    
    
def convert_time(time):
    hr, m=map(int, time.split(":"))
    
    converted_time=hr*60+m
    return converted_time


def solution(plans):
    answer = []
    plans.sort(key= lambda x:x[1])
    
    stack=[]
    
    for i in range(len(plans)):
        if i==len(plans)-1: # 마지막 수업
            answer.append(plans[i][0])


        else:
            plans[i][2]=int(plans[i][2])
            cur_time=convert_time(plans[i][1])
            next_time=convert_time(plans[i+1][1])

            left_time=next_time-cur_time
            
            if plans[i][2]<=left_time: # 다음 수업 시작 전에 끝내기 가능
                
                answer.append(plans[i][0])
                left_time-=plans[i][2] # 다음 수업 시작 전까지 남은 시간
                while stack:
                    plan_b=stack[-1]
                    # playtime > left_time
                    if plan_b[1]-left_time >0:
                        stack[-1][1]-=left_time
                        break
                    else:               
                        # playtime < left time
                        left_time-=plan_b[1]     
                        answer.append(plan_b[0])
                        stack.pop()

            else: # 불가능
                plans[i][2]-=left_time
                stack.append([plans[i][0], plans[i][2]]) # 과목명, 남은 시간 저장.
                


    while stack:
        answer.append(stack[-1][0])
        stack.pop()

    return answer


plans=[["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]

print(solution(plans))