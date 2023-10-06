# 이것이 코딩테스트다 편집 거리

A=input()
B=input()

long=0
short=0
if len(A)>=len(B):
    long=len(A)
    short=len(B)
else:
    long=len(B)
    short=len(A)

dp=[0]*(long+1)

i=0
j=0
k=1

while True:
    if i >=len(A):
        break

    elif j>=len(B):
        i+=1
        j=0

    else:

        if A[i]==B[j]:
            i+=1
            j+=1
            dp[k]=max(dp[k-1]+1, dp[k])
            k+=1

        else:
            j+=1
            

# print(len(B)-dp[k-1])
print(dp[k-1])

# time: 30분 25초