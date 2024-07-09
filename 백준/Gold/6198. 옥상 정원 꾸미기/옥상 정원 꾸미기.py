import sys

input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.reverse()

stack=[]
answer=[0]*(n)
for i in range(n):
    count=0
    prev_i=0
    while stack:
        if stack[-1][1]>=arr[i]:            
            break
        else:
            prev_i, _=stack.pop()
            # count+=1
            count+=answer[prev_i]+1
    # answer[i]=count+answer[prev_i]
    answer[i]=count
    stack.append((i,arr[i]))


# print(answer)
print(sum(answer))