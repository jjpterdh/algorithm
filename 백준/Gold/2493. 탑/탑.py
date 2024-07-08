import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))

# 순서가 존재(유지)
# 비교가 필요
# 풀이 방법: 스택으로 풀이
# 개수가 아니라... 제일 높은 탑의 인덱스를 출력..
ans=[0]*(n)
stack=[]
for i in range(n):
    while stack:
        if stack[-1][1]>arr[i]:
            
            ans[i]=stack[-1][0]+1
            break
        else:
            stack.pop()


    stack.append((i, arr[i]))

print(' '.join(map(str,ans)))


