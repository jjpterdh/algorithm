import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

s1=input().strip()
s2=input().strip()


d=[[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]

for i in range(1,len(s2)+1):
    for j in range(1, len(s1)+1):
        if s2[i-1]==s1[j-1]:
            d[i][j]=d[i-1][j-1]+1
        else:
            d[i][j]=max(d[i-1][j], d[i][j-1])

i=len(s2)
j=len(s1)
print(d[i][j])
ans=[]
while i>=0 and j>=0:
    
    if d[i-1][j]==d[i][j]:
        i-=1
    elif d[i][j-1]==d[i][j]:
        j-=1
    else:
        ans.append(s2[i-1])
        i-=1
        j-=1


for a in range(len(ans)-1, -1,-1):
    print(ans[a], end="")
