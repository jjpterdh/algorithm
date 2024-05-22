from queue import PriorityQueue

heap=PriorityQueue()
n=int(input())

for i in range(n):
    heap.put(int(input()))

total=0
while heap.qsize()>1:
    a=heap.get()
    b=heap.get()
    
    total+=(a+b)
    heap.put(a+b)

print(total)