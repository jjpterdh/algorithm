n,m=map(int, input().split())

mon=[]
for i in range(n):
    mon.append(int(input()))

d=[0]*10001

for i in range(1,m+1):
    for j in range(n):
        if mon[j] > i:
            continue

        if d[i-mon[j]]!=0:
            d[i]=d[i-mon[j]]+1


    if d[i]==0:
        d[i]=-1

print(d[m])

# 15min 소요시간