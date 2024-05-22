def solution(topping):
    length=len(topping)

    d1=[0]*length
    d2=[0]*length
    ele1=[0]*10001
    ele2=[0]*10001

    d1[0]=1
    ele1[topping[0]]=1
    d2[length-1]=1
    ele2[topping[-1]]=1

    count=0
    for i in range(1,length):
        if ele1[topping[i]]==0:
            ele1[topping[i]]=1            
            d1[i]=d1[i-1]+1
        else:
            d1[i]=d1[i-1]

    for i in range(length-2, -1, -1):
        if ele2[topping[i]]==0:
            ele2[topping[i]]=1
            d2[i]=d2[i+1]+1
        else:
            d2[i]=d2[i+1]

    for i in range(length-1):
        if d1[i]==d2[i+1]:
            count+=1

    
    answer=count
    
    return answer   



topping=[1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))