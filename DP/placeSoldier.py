# 백준 18353번 병사 배치하기

n=int(input())

army=list((map(int, input().split())))


narmy=[1]*n
for i in range(1, n):
    for j in range(i):
        if army[i] > army[j]:
            narmy[i]=max(narmy[i], narmy[j]+1)

print(max(narmy))

