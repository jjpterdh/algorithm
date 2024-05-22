import sys
sys.setrecursionlimit(10**6)

costs =     [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
            ,[7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
            ,[6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
            ,[7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
            ,[5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
            ,[4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
            ,[5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
            ,[3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
            ,[2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
            ,[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]



def solution(numbers):
    
    pos={(4,6):0, (6,4):0}
    
    for n in range(len(numbers)):
        num=int(numbers[n])
        new_pos={}
        for (L, R), total in pos.items():
            
            if L==num or R==num:
                result=min(new_pos.get((L,R), sys.maxsize), total+1)
                new_pos[(L, R)]=result
                new_pos[(R, L)]=result
            else:
                result1=min(new_pos.get((L,num), sys.maxsize), total+costs[R][num])
                result2=min(new_pos.get((R,num), sys.maxsize), total+costs[L][num])
                new_pos[(L, num)]=result1
                new_pos[(num, L)]=result1
                new_pos[(R, num)]=result2
                new_pos[(num, R)]=result2

        pos=new_pos
    return min(pos.values())
        

numbers="1756"	

print(solution(numbers))