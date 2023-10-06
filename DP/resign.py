
n= int(input())
T=[]
P=[]
for i in range(n):
    t, p= map(int, input().split())

    T.append(t)
    P.append(p)


sum=[0]*(n+1)

max_value=0
for i in range(n-1, -1, -1):
    time = T[i]+i
    if time <=n:
        sum[i]=max(P[i]+sum[time], max_value)
        max_value=sum[i]
    
    else:
        sum[i]=max_value

print(sum)



