import sys
from collections import deque

sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find_root(parent):
    for i in range(len(parent)):
        if parent[i]==-1:
            return i

n=int(input())
parent=list(map(int, input().split()))

root=find_root(parent)

del_node=int(input())
if parent[del_node]==-1:
    print(0)

else:
    parent[del_node]=-1
    visited=[False]*n
    ans=0
    tree={}
    for i in range(n):
        if tree.get(parent[i]) is None:
            tree[parent[i]]=[]
        
        tree[parent[i]].append(i)
    
    def dfs(x):
        global ans
        if tree.get(x) is None:
            ans+=1
        else:
            for node in tree[x]:
                if not visited[node]:
                    visited[node]=True
                    dfs(node)


        
    dfs(root)
    print(ans)