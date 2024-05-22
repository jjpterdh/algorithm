# 백준 수를 묶어서 최댓값 만들기
# 1744
from queue import PriorityQueue

pos=PriorityQueue()
neg=PriorityQueue()


n=int(input())


for _ in range(n):
    num=int(input())
    if num>0:
        pos.put(-num)
    else:
        neg.put(num)


sum=0
while pos.qsize()>1:
    data=-pos.get()
    data2=-pos.get()
    
    sum+=max(data+data2, data*data2)


while neg.qsize()>1:
    data=neg.get()
    data2=neg.get()
    
    sum+=max(data+data2, data*data2)

if not pos.empty() and not neg.empty():
    data=-pos.get()
    data2=neg.get()
    sum+=max(data+data2, data*data2)

elif pos.empty() and not neg.empty():
    sum+=neg.get()
elif not pos.empty():
    sum+=-pos.get()
print(sum)

