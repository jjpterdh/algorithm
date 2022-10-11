from collections import deque

n = int(input())
col = 2

d = [0] * 1001

d[0]=1
d[1]=3
for i in range(2, n):
    d[i] = (d[i-1]+(d[i-2]*2))%769679

print(d[n-1])
