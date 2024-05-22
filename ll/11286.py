from queue import PriorityQueue
import sys

input=sys.stdin.readline
n=int(input())
heap=PriorityQueue()





for i in range(n):
    x=int(input())
    
    if x==0:
        if heap.empty():
            print(0)
        else:
            temp=heap.get()
            print(temp[1])

    else: #배열에 추가
        heap.put((abs(x), x))



