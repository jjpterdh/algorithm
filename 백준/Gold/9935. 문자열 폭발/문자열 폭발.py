import sys
input =sys.stdin.readline

sent=input().strip()
pattern=input().strip()
n=len(pattern)
new_sent=[]

for s in sent:
    new_sent.append(s)
    if pattern[-1]==s and pattern==''.join(new_sent[-n:]):    
        for _ in range(n):
            new_sent.pop()
    
    





if new_sent:
    print("".join(new_sent))
else:
    print('FRULA')