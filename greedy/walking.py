import sys
input=sys.stdin.readline

def smaller(x,y,w,s):
    big=max(x,y)
    small=min(x,y)
    answer=0
    if s <= w:
        if (big%2==0 and small%2==0) or (big%2!=0 and small%2!=0):
            answer=big*s
        else:
            answer+=(big-1)*s
            answer+=w
            

        return answer

    else:
        answer=min((x*w)+(y*w), (small*max(s,w))+((big-small)*min(s,w)))
        return answer

x, y, w, s= map(int, input().split())

answer=0
answer=smaller(x,y,w,s)
print(answer)


