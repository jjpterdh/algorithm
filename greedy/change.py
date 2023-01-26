arr=[500, 100, 50, 10, 5, 1]

change=int(input())
change=1000-change



count = 0
for i in range(6):
    if change >= arr[i]:
        n=change//arr[i]
        change-=n*arr[i]
        count+=n

print(count)