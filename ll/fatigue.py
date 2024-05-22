from itertools import permutations



def solution(k, dungeons):
    answer = -1
    
    for p in permutations(dungeons, len(dungeons)):
        tmp=k
        cnt=0

        for need,spend in p:
            if tmp>=need:
                tmp-=spend
                cnt+=1
        answer=max(answer, cnt)
    


    return answer

k=80
dungeons=[[80,20],[50,40],[30,10]]	
print(solution(k,dungeons))