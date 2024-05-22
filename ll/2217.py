import sys
from queue import PriorityQueue
answer=0
input=sys.stdin.readline
n=int(input())
roaps=PriorityQueue()
for i in range(n):
    roaps.put(int(input()))


while not roaps.empty():
    weight=roaps.get()
    answer=max(answer, (weight*(roaps.qsize()+1)))

print(answer)