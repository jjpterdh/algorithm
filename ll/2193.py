import sys
input=sys.stdin.readline

n=int(input())
d=[[0]*(n+1) for _ in range(2)]


d[0][1]=0
d[1][1]=1
# print(d[2][0])
for i in range(2, n+1):
    
    d[0][i]=d[0][i-1]+d[1][i-1]
    d[1][i]=d[0][i-1]
    

total=d[0][n]+d[1][n]
print(total)