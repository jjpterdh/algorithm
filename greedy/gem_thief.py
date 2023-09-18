import heapq
import sys
input=sys.stdin.readline

# input
N, K= map(int, input().split())
gem=[list(map(int, input().split())) for i in range(N)]
bag=[int(input()) for i in range(K)]


# answer
answer=0
# sort
bag.sort()
gem.sort()
temp=[]
for i in bag:
    while gem and i>=gem[0][0]:
        heapq.heappush(temp, -gem[0][1])
        heapq.heappop(gem)
    
    if temp:
        answer+=heapq.heappop(temp)
    elif not gem:
        break
print(-answer)
