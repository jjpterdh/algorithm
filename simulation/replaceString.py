# Facebook interview

sent=input()
new_sent=[0]*24

sum=0

for i in range(len(sent)):
    if ord(sent[i]) <ord('A'):
        sum+=int(sent[i])
    
    else:
        index=ord(sent[i])-ord('A')
        
        new_sent[index]+=1


for i in range(len(new_sent)):
    for j in range(new_sent[i]):
        print(chr(i+65), end='')

print(sum)