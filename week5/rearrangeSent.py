from collections import deque

sent=list(input())
sent.sort()

i=0
sum=0
while '0'<=sent[i] and sent[i] <='9':
    sum += int(sent[i])
    i+=1
for j in range(i, len(sent)):
    print(sent[j], end='')
print(sum)