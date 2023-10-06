n=input()


dis=len(n)



sum1=0
sum2=0

for i in range(dis//2):
    sum1+=int(n[i])
    sum2+=int(n[dis-1-i])



if sum1==sum2:
    print("LUCKY")
else:
    print("READY")
    
