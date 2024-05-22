from queue import PriorityQueue
def solution(k, tangerine):
    heap=PriorityQueue()
    answer = 0
    tree={}
    for i in tangerine:
        if tree.get(i) is None:
            tree[i]=0
        tree[i]+=1

    
    for value in tree.values():
        
        heap.put(-value)
    count=0
    while not heap.empty() and k>0:
        count+=1
        k+=heap.get()

    answer=count

    return answer



k=6
tangerine=[1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))