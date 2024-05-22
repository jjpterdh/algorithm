import sys

input=sys.stdin.readline

n,m,k=map(int, input().split())


treeHeight=0
length=n
while length!=0:
    length//=2
    treeHeight+=1


treeSize=pow(2, treeHeight+1)
leftNodeStartIndex=treeSize//2 -1
tree=[0]*(treeSize+1)

# tree[leftNodeStartIndex:leftNodeStartIndex+len(arr)]=arr[:]
for i in range(leftNodeStartIndex+1, leftNodeStartIndex+n+1):
    tree[i]=int(input())

def makeTree(i):
    while i!=1:
        tree[i//2]+=tree[i]
        i-=1

makeTree(treeSize-1)



def updateTree(idx,value):
    diff=value-tree[idx]
    while idx>0:
        tree[idx]+=diff
        idx//=2


def getSum(s, e):
    partsum=0
    while s<=e:
        if s%2==1:
            partsum+=tree[s]
            s+=1
        if e%2==0:
            partsum+=tree[e]
            e-=1
        
        s=s//2
        e=e//2

    return partsum


for _ in range(m+k):
    a,b,c=map(int, input().split())
    if a==1:
        #b -> c로
        updateTree(leftNodeStartIndex+b,c)

    else:
        # b~c 구간 합
        s=b+leftNodeStartIndex
        e=c+leftNodeStartIndex
        print(getSum(s,e))
