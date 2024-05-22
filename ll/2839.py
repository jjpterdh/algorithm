import sys
input=sys.stdin.readline

n=int(input())
count=sys.maxsize

if n%5!=0:
    num=n//5
    for i in range(1, num+1):
        new_count=0
        tmp=n-(5*i)
        if tmp%3==0:
            new_count+=i
            new_count+=tmp//3

            count=min(count, new_count)

    num=n//3
    for i in range(1, num+1):
        new_count=0
        tmp=n-(3*i)
        if tmp%5==0:
            new_count+=i
            new_count+=tmp//5
            count=min(count, new_count)
    if count==sys.maxsize:
        print(-1)
    else:
        print(count)
else:
    print(n//5)

