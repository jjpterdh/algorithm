from collections import deque
import sys

input=sys.stdin.readline

n,k=map(int, input().split())

money=[int(input()) for _ in range(n)]

count=0
while k:
    for coin in reversed(money):
        if k>=coin:
            count+=k//coin
            k%=coin
            break
        elif coin>=k:
            money.remove(coin)
    
print(count)