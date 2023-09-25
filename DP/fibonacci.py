# 이것이 코딩테스트다
n=int(input())

d=[0]*100

def fibonacci(n, d):
    
    if n<=2:
        return 1
    
    if d[n]!=0:
        return d[n]
    
    else:
        d[n]= fibonacci(n-1, d)+fibonacci(n-2,d)
        return d[n]

print(fibonacci(n, d))