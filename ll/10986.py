import sys

input=sys.stdin.readline

n,m=map(int, input().split())
arr=list(map(int, input().split()))

S=[]
C=[0]*m


sum=0
for i in range(len(arr)):
    sum+=arr[i]
    S.append(sum)

count=0
for i in range(len(arr)):
    remainder=S[i]%m
    if remainder==0:
        
        count+=1
    
    C[remainder]+=1


ans=count


for i in range(m):
    if C[i]>1:
        ans+=(C[i]*(C[i]-1)//2)



print(ans)

