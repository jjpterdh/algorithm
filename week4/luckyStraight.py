n = int(input())

# print(len(str(n)))
arr=list(str(n))

sum1=0
sum2=0
for i in range(len(arr)):
    # print(arr[i])

    if i < (len(arr)/2):
        sum1+=int(arr[i])
    else:
        sum2+=int(arr[i])


if sum1==sum2:
    print('LUCKY')

else:
    print("READY")