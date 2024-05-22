import sys
input=sys.stdin.readline

node, edge=map(int, input().split())

parent=[i for i in range(node+1)]

def find(x):
    if parent[x]==x:
        return x
    
    parent[x]=find(parent[x])       
    return parent[x]

def union(a, b):
    a=find(a)
    b=find(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b


for i in range(edge):
    u, v=map(int, input().split())
    union(u,v)

count=0
checked=[0]*(node+1)

for i in range(1,len(parent)):
    
    if checked[find(parent[i])]==0:
        count+=1
        checked[find(parent[i])]+=1


print(count)

