import math
n,k=map(int, input().split())
sum=0

while n>1:
    if n%k==0:
        sum+=1
        n=n/k
    else:
        sum+=n%k
        n=n-(n%k)

print(sum)