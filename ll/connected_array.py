# 슬라이딩 윈도우

def solution(sequence, k):
    
    
    sequence=sorted(sequence)
    s=0
    e=0
    real_s=0
    real_e=1000001
    total=sequence[0]

    while e<len(sequence) and s<=e:
        
        if total<k:
            e+=1
            if e<len(sequence):                
                total+=sequence[e]
            
        elif total>k:
            total-=sequence[s]
            s+=1

        else:
            if real_e-real_s > e-s:
                real_e=e
                real_s=s
            total-=sequence[s]
            s+=1

    answer=[real_s,real_e]    
    return answer



sequence=[2, 2, 2, 2, 2]
k=6
print(solution(sequence, k))
