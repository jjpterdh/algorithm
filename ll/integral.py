def rainy(k):
    x=0
    arr=[(x,k)]

    while k>1:
        x+=1
        if k%2==0:
            k//=2
        else:
            k*=3
            k+=1
        arr.append((x,k))
    
    return arr


def solution(k, ranges):
    answer = []
    arr=rainy(k)
    for s,e in ranges:
        total=0
        if s==0 and e==0:
            for i in range(len(arr)-1):
                height=arr[i][1]+arr[i+1][1]
                total+=height/2
        else:
            if s>len(arr)-1+e:
                total=-1
            else:
                for i in range(s,len(arr)+e-1):
                    height=arr[i][1]+arr[i+1][1]
                    total+=height/2


        answer.append(float(total))
    return answer

k=5
ranges=[[0,0],[0,-1],[2,-3],[3,-3]]

print(solution(k, ranges))