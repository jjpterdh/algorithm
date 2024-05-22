import sys
input=sys.stdin.readline
inf=1e9
n=int(input())
w=[]
for i in range(n):
    w.append([])
    w[i]=list(map(int, input().split()))

d=[[0 for i in range(1<<16)] for i in range(16)]

def tsp(c,v):
    if v==(1<<n)-1:
        if w[c][0]==0:
            return inf
        else:
            return w[c][0]
    if d[c][v]!=0:
        return d[c][v]
    
    min_val=inf
    for i in range(0,n):
        if(v&(1<<i))==0 and w[c][i]!=0:
            min_val=min(min_val, tsp(i,(v | (1<<i)))+w[c][i])
    
    d[c][v]=min_val
    return d[c][v]

print(tsp(0,1))

