# 백준 12891번 문제

DNA={'A':0, 'C':1, 'G':2, 'T':3}

n,window=map(int, input().split())
password=list(input())
condition=list(map(int, input().split()))

count=0
temp=[0]*4

# first time
for i in range(window):
    temp[DNA[password[i]]]+=1
    aa=1
    for k in range(4):
        if temp[k]< condition[k]:
            aa=0
            break
    count+=aa
    

# second time
for i in range(1, n):
    print(temp)
    if i+window>n:
        break
    
    temp[DNA[password[i-1]]]-=1
    temp[DNA[password[i+window-1]]]+=1
    
    aa=1
    for k in range(4):
        if temp[k]< condition[k]:
            aa=0
            break

    count+=aa


    
    

print(count)