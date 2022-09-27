import time
#list_name.sort()
start_time=time.time()
# input
n, m ,k=map(int, input().split())
arr=[]
arr.extend(map(int, input().split()))
arr.sort()


total=0
flag=0
start=0

for i in range(m):

    for j in range(k):
        pos=n-1
        if start>=m:
            break        
        elif flag==3:
            pos-=1
            flag=0

        total+=arr[pos]
        print(arr[pos])
        start+=1
        flag+=1
        

    

print(total)

end_time=time.time()