import sys
from itertools import permutations
input=sys.stdin.readline
n,m = map(int, input().split())

arr=[i for i in range(1,n+1)]
ans=list(permutations(arr, m))


for num in ans:
    for k in num:
        print(k, end=' ')
    print()
    