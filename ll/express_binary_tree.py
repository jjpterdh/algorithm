from collections import deque

def convert_bin(num):
    arr=deque([])
    while num:
        arr.append(num%2)
        num//=2
    
    arr.reverse()

    if len(arr)%2==0:
        arr.appendleft(0)
    arr.appendleft(0)
    return arr

def solution(numbers):
    answer = []
    for num in numbers:
        nodes=convert_bin(num)
        print(nodes)
        # preorder로 트리 표현하기 
        answer.append(1)
        for idx in range(1, len(nodes)):
            
            if idx%2==0 and nodes[idx]==0:
                answer[-1]=0
                break
        

    return answer   


numbers=[7, 42, 95]
print(solution(numbers))