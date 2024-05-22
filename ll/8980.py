import sys

input=sys.stdin.readline

n,capacity=map(int, input().split())
m=int(input())
cities=[]
truck=[0]*(n+1)
answer=0
weight=0

for i in range(m):
    start, end, box=map(int, input().split())
    cities.append([start, end ,box])


cities.sort(key=lambda x:(x[1], x[0]))

for start,end,box in cities:
    temp=box
    for i in range(start, end):
        if truck[i]+temp>=capacity:
            temp=capacity-truck[i]
    
    for i in range(start,end):
        truck[i]+=temp
    
    answer+=temp

    

print(answer)
