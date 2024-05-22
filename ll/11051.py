import sys
input=sys.stdin.readline

mod=10007

n,k=map(int, input().split())
d=[0]*(n+1)
d[0]=1
for i in range(1,n+1):
    d[i]=d[i-1]*i

# print(d)
print((d[n]//(d[n-k]*d[k]))%mod)
