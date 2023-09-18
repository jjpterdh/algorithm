import sys

input=sys.stdin.readline



t=int(input())
for i in range(t):
    box=20
    empty=0
    n=int(input())

    home=list(map(int, input().split()))
    market=[list(map(int, input().split())) for _ in range(n) ]

    festival=list(map(int, input().split()))

    print(home)
    print(market)
    print(festival)
