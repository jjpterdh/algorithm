# 이것이 코딩 테스트다

n= int(input())

count=0

# print(133%10)

for h in range(n+1):
    for m in range(60):
        for s in range(60):

            if '3'in str(h)+str(m)+str(s):
                count+=1

print(count)
