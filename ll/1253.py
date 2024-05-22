import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
arr.sort()
count=0
for i in range(n):
    s=0
    e=n-1 # 마이너스가 있을 수도 있음
    while s<e:
        


        if arr[i]>arr[s]+arr[e]:
            s+=1
        elif arr[i]< arr[s]+arr[e]:
            e-=1
        else:
            # 중복? 있으면 고민해야함
            if s!=i and e!=i:
                count+=1
                break
            elif s==i:
                s+=1
            
            elif e==i:
                e-=1
            

print(count)