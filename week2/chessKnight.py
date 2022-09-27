#knight movement
rows=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
firstMov=[-2, 2]
secMov=[-1, 1]

pos=input()

# x,y 구하기
x=0
for i in range(len(rows)):
    if pos[0]==rows[i]:
        x=i+1

y=int(pos[1])

# 경우의 수 구하기
count=0
for i in range(2):

    if i==0: # x축으로 이동
       for first in firstMov:
            tmpx=x
            tmpy=y
            tmpx=tmpx+int(first)
            for sec in secMov:
                tmpy=tmpy+int(sec)

                if tmpx >0 and tmpy >0:
                    count+=1
    else: # y축으로 이동
        for first in firstMov:
            tmpx=x
            tmpy=y
            tmpy=tmpy+int(first)
            for sec in secMov:
                tmpx=tmpx+int(sec)

                if tmpx >0 and tmpy >0:
                    count+=1
    

print(count)