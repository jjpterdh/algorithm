import sys
inf=sys.maxsize

input=sys.stdin.readline



n,m=map(int,input().split())

treeHeight=0
length=n
while length>0:
    length//=2
    treeHeight+=1


treeSize=pow(2, treeHeight+1)
leftNodeStartIndex=treeSize//2-1

tree=[inf]*(treeSize+1)
for i in range(leftNodeStartIndex+1, leftNodeStartIndex+n+1):
    tree[i]=int(input())

def setTree(i):
    while i!=1:
        tree[i//2]=min(tree[i//2], tree[i])
        i-=1


setTree(treeSize-1)

def getMin(s,e):
    ans=inf

    while s<=e:
        if s%2==1:
            ans=min(ans, tree[s])
            s+=1
        if e%2==0:
            ans=min(ans, tree[e])
            e-=1
        s//=2
        e//=2

    return ans

ans=[]
for i in range(m):
    a,b=map(int, input().split())
    
    a+=leftNodeStartIndex
    b+=leftNodeStartIndex
    print(getMin(a,b))
    # ans.append(getMin(a,b))

# print(ans)
