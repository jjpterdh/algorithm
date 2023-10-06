# 이것이 코딩테스트다

n=int(input())

arr=[1] * n

q=0
w=0
e=0

for i in range(1,n):

    arr[i]=min(arr[q]*2, arr[w]*3, arr[e]*5)

    if arr[i]==arr[q]*2:
        q+=1


    if arr[i]==arr[w]*3:
        w+=1

    if arr[i]==arr[e]*5:
        e+=1

    
        


print(arr)
print(arr[n-1])
print(q,w,e)


# time: 