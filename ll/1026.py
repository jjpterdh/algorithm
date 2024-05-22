import sys

input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
A.sort()
B=list(map(int,input().split()))
B.sort(reverse=True)

answer=0
for i in range(n):
    answer+=A[i]*B[i]

print(answer)