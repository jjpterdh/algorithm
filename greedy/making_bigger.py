import sys

input=sys.stdin.readline

n,k=map(int, input().split())
num=input().strip()



tmp=[]
for n in num:
    while tmp and tmp[-1] < n and k > 0:
        tmp.pop()
        k-=1
    tmp.append(n)

if k > 0:
    print(''.join(tmp[:-k]))
else:
    print(''.join(tmp))

# print(tmp)

