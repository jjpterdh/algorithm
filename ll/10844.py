import sys

input=sys.stdin.readline
inf=1000000000
n=int(input())

d=[[0 for _ in range(n+1)] for _ in range(10)]


for i in range(1,10):
    d[i][1]=1



for i in range(2,n+1):
    
    d[0][i]=d[1][i-1]
    d[9][i]=d[8][i-1]
    for j in range(1, 9):
        d[j][i]=(d[j-1][i-1]+d[j+1][i-1])%inf


    

total=0

for i in range(10):
    total+=(d[i][n])
    total%=inf
print(total%inf)