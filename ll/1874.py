import sys

input=sys.stdin.readline
n=int(input())

arr=list(int(input()) for _ in range(n))
flag=True
idx=0
count=2
cur=0
stack=[1]
ans=['+']
while idx<n:
    
    
    if not stack:
        stack.append(count)
        ans.append("+")
        count+=1
    else:
        if stack[-1]>arr[idx]:
            flag=False
            break

        elif stack[-1]==arr[idx]:
            ans.append('-')
            stack.pop()
            idx+=1
        
        else:
            stack.append(count)
            ans.append("+")
            count+=1


if flag:
    for a in ans:
        print(a)

    
else:
    print("NO")