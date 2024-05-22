import sys
from collections import deque

input=sys.stdin.readline

n=int(input())

tree={}
for _ in range(n):
    parent, child1, child2=input().strip().split()
    if tree.get(parent) is None:
        tree[parent]=[child1, child2]



def preorder(root):

    print(root, end='')
    for node in tree[root]:
        if node=='.':
            continue
        preorder(node)


def inorder(root):
    if tree[root][0]!='.':
        inorder(tree[root][0])
    print(root, end='')
    if tree[root][1]!='.':
        inorder(tree[root][1])

def postorder(root):
    if tree[root][0]!='.':
        postorder(tree[root][0])
    
    if tree[root][1]!='.':
        postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')