import sys
input=sys.stdin.readline
inf=1e9
n=int(input())
d=[0]*(10**6+1)

temp=2
d[1]=0
while temp<=n:
    a=inf
    b=inf
    c=inf
    if temp%2==0:
        a=d[temp//2]
    
    if temp%3==0:
        b=d[temp//3]
    
    if temp>1:
        c=d[temp-1]


    d[temp]=min(a+1, b+1, c+1)
    
    
    temp+=1



    

print(d[n])