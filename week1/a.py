#1부터 N까지의 M의 배수합
import time


start_time=time.time()

n=int(input("N을 입력해주세요: "))
m=int(input("M을 입력해주세요: "))

total=0
for i in range(n):
    if (i+1)%m==0:
        total+=(i+1)




end_time=time.time()
print(total)
print("time: ", end_time-start_time)