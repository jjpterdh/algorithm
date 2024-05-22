

def solution(picks, minerals):
    answer=0
    sum=0
    # 곡괭이의 수를 구한다.    
    for i in picks:        
        sum += i        
    
    #곡괭이로 캘 수 있는 광물만큼 자른다.    
    num = sum * 5    
    if len(minerals)>sum:        
        minerals = minerals[:num]

    #광물들을 조사한다.
    new_minerals =[[0,0,0] for _ in range((len(minerals) //5 +1))]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_minerals[i//5][0]+=1
        elif minerals[i]=='iron':
            new_minerals[i//5][1]+=1
        elif minerals[i]=='stone':
            new_minerals[i//5][2]+=1


    #광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    
    new_minerals.sort(key=lambda x:(x[0],x[1],x[2]), reverse=True)
    
    #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in new_minerals:
         dia,iron,stone = i
         for j in range(len(picks)):
            if picks[j]>0 and j==0:
                picks[j]-=1
                answer += dia + iron + stone
                break
            elif picks[j]>0 and j==1:
                picks[j]-=1
                answer += (5*dia) + iron + stone
                break
            elif picks[j]>0 and j==2:
                picks[j]-=1
                answer += (25*dia) + (5*iron) + stone
                break

    return answer







picks=[0, 1, 1]
minerals=["iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]
print(solution(picks, minerals))