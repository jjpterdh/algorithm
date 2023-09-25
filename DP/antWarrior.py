# 이것이 코딩테스트다
n=int(input())

food=list(map(int, input().split()))

a=[0]*100
a[0]=food[0]
a[1]=max(food[0], food[1])
for i in range(2, n):
    a[i]=max(a[i-1], a[i-2]+food[i])
        
a[n]=max(a[n-2]+food[n-1], a[n-1])        
print(a[n-1])

# time: 22분 16초