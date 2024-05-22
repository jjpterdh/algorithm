import sys

input=sys.stdin.readline

n=int(input())
M=[]
M.append((0,0))
D=[[-1 for j in range(n+1)] for i in range(n+1)]

for i in range(n):
    a,b=map(int, input().split())
    M.append((a,b))

def execute(a,b):
    result=sys.maxsize

    if D[a][b]!=-1:
        return D[a][b]
    
    if a==b:
        return 0
    elif a+1==b:
        return M[a][0]*M[a][1]*M[b][1]

    for i in range(a,b):
        result=min(result, M[a][0]*M[i][1]*M[b][1]+execute(a,i)+execute(i+1,b))
    
    D[a][b]=result
    return D[a][b]

print(execute(1,n))
