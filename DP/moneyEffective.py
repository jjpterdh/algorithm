# 이것이 코딩테스트다

# input 
n,m=map(int, input().split())
money=[int(input()) for _ in range(n)]



a=[100000]*(m+1)

for i in range(len(money)):
    if money[i]>m:
        continue
    a[money[i]]=1

for i in range(1, m+1):
    for j in range(len(money)):
        if i-money[j]>=0 and a[i-money[j]]!=100000:
            
            
            a[i]=min(a[i], a[i-money[j]]+1)
        

        
if a[m]==100000:
    print(-1)

else:
    print(a[m])







    