import sys
from queue import PriorityQueue

heap=PriorityQueue()
input=sys.stdin.readline


def solution(heap, n):
    
    count=0
    end=-1
    for i in range(n):
        e, s=heap.get()
        
        if s>=end:
            count+=1
            end=e

    return count


n=int(input())

for i in range(n):
    start,end=map(int, input().split())
    heap.put((end, start))


print(solution(heap, n))
