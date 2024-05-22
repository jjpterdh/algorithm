import sys
# input=sys.stdin.readline

expression=input()
expression_list=list(expression.split("-"))

ans=0
for plus in expression_list[0].split("+"):
    ans+=int(plus)

for minus in expression_list[1:]:
    
    total=0
    for plus in minus.split("+"):
        total+=int(plus)
    
    ans-=total

    
print(ans)