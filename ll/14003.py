import sys
input=sys.stdin.readline
n=int(input())
A=list(map(int, input().split()))
A.insert(0,0)

index=0
maxLength=1
B=[0]*1000001
D=[0]*1000001
ans=[0]*1000001
B[maxLength]=A[1]
D[1]=1


def binarySearch(l, r, now):
    while l<r:
        mid=(l+r)//2
        if B[mid]<now:
            l=mid+1
        else:
            r=mid
    
    return l

for i in range(2,n+1):
    if B[maxLength] < A[i]:
        maxLength+=1
        B[maxLength]=A[i]
        D[i]=maxLength

    else:
        index=binarySearch(1, maxLength, A[i])
        B[index]=A[i]
        D[i]=index

print(maxLength)
index=maxLength
x=B[maxLength]+1


for i in range(n, 0,-1):
    if D[i]==index:
        ans[index]=A[i]
        index-=1


for i in range(1, maxLength+1):
    print(ans[i], end=' ')