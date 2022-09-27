#use min(), max()


n,m=map(int, input().split())

small_i=0
a=[]
# for i in range(n):
#     a.append(list(map(int, input().split())))
#     small_j=100000
#     for j in range(m):
#         if small_j>a[i][j]:
#             small_j=a[i][j]
#     if small_i<small_j:
#         small_i=small_j

result=0
for i in range(n):
    data= list(map(int, input().split()))
    min_val=min(data)
    result=max(result, min_val)

print(result)


