import sys

input=sys.stdin.readline
n=int(input())
arr=[0]*(1232)
def convert_date(sm,sd,em,ed):
    return (int(sm+sd), int(em+ed))

flowers=[]
for i in range(n):
    sm,sd,em,ed=(input().split())    
    date=convert_date(sm,sd,em,ed)
    flowers.append(date)

flowers.sort(key=lambda x: (x[0], x[1]))
print(flowers)
answer=0







