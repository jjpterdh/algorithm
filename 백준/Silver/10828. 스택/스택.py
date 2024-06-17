import sys

input= sys.stdin.readline

n=int(input())
arr=[]


def push(arr, num):
    arr.append(num)
    return


def pop(arr):

    if arr==[]:
        return -1
    return arr.pop()


def size(arr):
    return len(arr)

def empty(arr):
    if arr==[]:
        return 1
    else:
        return 0

def top(arr):
    if empty(arr):
        return -1
    return arr[-1]

for i in range(n):
    string=input()
    command=string.split()[0]
    if command=="push":
        num=int(string.split()[1])
        push(arr, num)

    elif command=="pop":
        print(pop(arr))

    elif command=="size":
        print(size(arr))

    elif command=="empty":
        print(empty(arr))

    else:
        print(top(arr))



