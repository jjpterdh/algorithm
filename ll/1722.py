import sys
input=sys.stdin.readline
n=int(input())
arr=[i for i in range(1,n+1)]
prob=[0]*(n+1)
prob[0]=1
S=[0]*21
visited=[False]*21
for i in range(1,n+1):
    prob[i]=prob[i-1]*i

num=list(map(int, input().split()))

flag=num[0]
compare=num[1:]

if flag==1:
    
    for i in range(1,n+1):
        cnt=1
        for j in range(1,n+1):
            if visited[j]:
                continue
            if num[1]<=cnt*prob[n-i]:
                num[1]-=(cnt-1)*prob[n-i]
                S[i]=j
                visited[j]=True
                break
            cnt+=1

    for i in range(1,n+1):
        print(S[i], end=' ')

else:
    K=1
    for i in range(1,n+1):
        cnt=0
        for j in range(1, num[i]):
            if not visited[j]:
                cnt+=1
        K+=cnt*prob[n-i]
        visited[num[i]]=True
    print(K)



