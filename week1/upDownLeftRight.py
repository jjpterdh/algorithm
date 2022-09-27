# n=int(input())

# move=input().split()

# x=1
# y=1
# for i in range(len(move)):
#     if move[i]=='R': # right
#         if x+1<=n:
#             x+=1
#     elif move[i]=='U': # up
#         if y-1>=1:
#             y-=1
#     elif move[i]=='D': # down
#         if y+1<=n:
#             y+=1
#     else:
#         if x-1>=1: # left
#             x-=1

# print(y, x)


n=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    
    x,y=nx,ny

print(x,y)