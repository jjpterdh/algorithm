import sys
input=sys.stdin.readline

n=int(input())

arr=list(map(int, input().split()))
arr.sort()

cnt=0
for k in range(len(arr)):
    start=0
    end=len(arr)-1
    while start<end:
        if arr[k] > arr[start]+arr[end]:
            start+=1

        # 
        elif arr[k] < arr[start]+ arr[end]:
            end-=1

        
        else:
            if start==k:
                start+=1

            elif end==k:
                end-=1

            else:
                cnt+=1
                break
            
            
            
            

print(cnt)