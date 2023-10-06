n=int(input())

d=[0]*1001

odd=True
if n%2==0:
    odd=False

d[1]=1
d[2]=3

for i in range(3, n+1):
    d[i]=d[i-1]+d[i-2]*2

print(d[i]%796796)





# time: 09:18