inf=1000000001
from queue import PriorityQueue

def solution(n, k, enemy):
    answer = len(enemy)
    heap=PriorityQueue()


    for i in range(len(enemy)):
        heap.put(-enemy[i])
        n-=enemy[i]
        
        if n<0 and k>0:
            k-=1
            n+=-heap.get()
        
        elif n<0 and k<=0:
            answer=i
            break
        



    return answer





n=2
k=4
enemy=[3, 3, 3, 3]


print(solution(n,k,enemy))