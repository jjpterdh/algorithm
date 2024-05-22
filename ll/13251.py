import sys


input=sys.stdin.readline
m=int(input())
n=list(map(int, input().split()))
total=0
for i in range(m):
    
    total+=n[i]
    
k=int(input())

d=[0]*(total+1)
d[0]=1
for i in range(1,total+1):
    d[i]=d[i-1]*i

answer=0
total_prob=d[total]//(d[total-k]*d[k])
prob=0
for num in n:
    prob+=d[num]//(d[num-k]*d[k])

answer=prob/total_prob
print(answer)








