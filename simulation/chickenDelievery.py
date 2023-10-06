# 백준 15686 치킨 배달
from itertools import combinations

n,m=map(int, input().split())

board=[list(map(int, input().split())) for _ in range(n)]

houses=[]
chickens=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            houses.append((i+1, j+1))
        
        elif board[i][j]==2:
            chickens.append((i+1, j+1))


candidates=list(combinations(chickens, m))



total=0
def get_sum(candidate):
    result=0

    for hy, hx in houses:
        temp=1e9
        for cy, cx in candidate:
            temp=min(temp, abs(hx-cx)+abs(hy-cy))

        result+=temp

    return result

result=1e9

for candidate in candidates:
    result= min(result, get_sum(candidate))

print(result)