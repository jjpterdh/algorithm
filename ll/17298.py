n=int(input())

arr=list(map(int, input().split()))

stack=[]
ans=[0]*n

for i in range(n):

    if not stack:
        stack.append(i)


    else:
        while stack and arr[i]>arr[stack[-1]]:
            ans[stack[-1]]=arr[i]
            stack.pop()


        stack.append(i)


while stack:
    ans[stack[-1]]=-1
    stack.pop()


for i in ans:
    print(i, end=' ')