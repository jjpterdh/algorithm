import sys

input=sys.stdin.readline
n= int(input())
row=[0]*(n+1)
answer=0

def check(x):
    for i in range(x):
        if row[i]==row[x] or abs(row[i]-row[x])==abs(x-i):
            return False
    
    return True


def dfs(count):   
    global answer
    if count==n:
        answer+=1
        
    else:
        for i in range(n):
            #[count, i] 위치에 배치
            row[count]=i

            if check(count):
                dfs(count+1)


dfs(0)
print(answer)