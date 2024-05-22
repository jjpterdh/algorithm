import sys

input=sys.stdin.readline
n,m,k=map(int, input().split())
num=1000000007
length=n
treeHeight=0

while length:
    length//=2
    treeHeight+=1

treeSize=pow(2, treeHeight+1)
leftNodeStartIndex=treeSize//2-1
tree=[1]*(treeSize+1)
for i in range(leftNodeStartIndex+1, leftNodeStartIndex+n+1):
    tree[i]=int(input())

def setTree(i):
    while i!=1:
        tree[i//2]*=tree[i]%num
        i-=1



setTree(treeSize-1)

def updateTree(b, c):
    tree[b]=c

    while b>1:
        b//=2
        tree[b]=tree[2*b]%num * tree[2*b+1]%num

def getMul(s,e):
    ans=1

    while s<=e:
        if s%2==1:
            ans*=tree[s]
            s+=1
        if e%2==0:
            ans*=tree[e]
            e-=1
        
        s//=2
        e//=2

    return ans
ans=[]

for _ in range(m+k):
    i=0
    a,b,c=map(int, input().split())

    if a==1:
        b+=leftNodeStartIndex
        updateTree(b,c)
        
    else:
        s=b+leftNodeStartIndex
        e=c+leftNodeStartIndex
        print(int(getMul(s,e))%num)
        # ans.append(int(getMul(s,e)%num))

# print(ans)