def checkBuild(answer):
    
    for anw in answer:
        x,y,a=anw
        
        if a==0: # 기둥
            if y==0: # 바닥
                continue
            
            elif [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
                
            else:
                return False
            
        else: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer: # 아래 기둥 확인
                
                continue
            
            elif [x-1, y, 1] in answer and [x+1, y, 1] in answer: # 양 옆에 보 확인
                continue
            else:
                return False
            
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, a, b=frame        
        
        
        if b==0: # 삭제
            answer.remove([x,y,a])
            
            if not checkBuild(answer):
                answer.append([x,y,a])
        
    
        else: # 설치
            answer.append([x,y,a])
            
            if not checkBuild(answer):
                answer.remove([x,y,a])
                
                
    
    answer.sort()
    # print(answer)
    return answer
        
        
        
