import sys
input=sys.stdin.readline


t=int(input())
for _ in range(t):
    
    k=int(input())
    n=int(input())
    apartment=[[0]*15 for _ in range(15)]
    
    # 아파트 초기화    
    for j in range(1,n+1):
        apartment[0][j]=j

    for i in range(1,k+1):
        for j in range(1,n+1):
            apartment[i][j]+=(apartment[i-1][j]+apartment[i][j-1])

    # print(apartment)
    print(apartment[k][n])
    

