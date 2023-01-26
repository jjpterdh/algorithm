
def solution(n, ramen):
    answer=0
    i=0
    
    while True:
        count=0
        cond=0
        if i >=n:
            break

        if ramen[i]==0:
            i+=1
            continue
        else:
            j=i+1
            cond=3
            for k in range(2): # 몇번째 조건인지 구하기
                
                if j+k < n+2 and ramen[j+k]==0:
                    break
                
                elif j+k < n+2:
                    if k==0:
                        cond=5
                    elif k==1:
                        cond=7
                else:
                    break
            # print(cond)

            # 조건에 따라 라면 사기
            if cond==3:
                count+=cond*ramen[i]
                ramen[i]=0

            elif cond==5:
                if ramen[i]>ramen[i+1]:
                    dif=ramen[i]-ramen[i+1]
                    count+=dif*3
                    ramen[i]-=dif
                count+=ramen[i]*cond
                ramen[i+1]-=ramen[i]
                ramen[i]=0
            
            else:
                if ramen[i+1]> ramen[i+2]:
                    min_cost=min(ramen[i], ramen[i+1]- ramen[i+2])
                    count+=5*min_cost
                    ramen[i]-=min_cost
                    ramen[i+1]-=min_cost
                    

                min_cost=min(ramen[i], ramen[i+1], ramen[i+2])
                count+=cond*min_cost
                ramen[i]-=min_cost
                ramen[i+1]-=min_cost
                ramen[i+2]-=min_cost

            answer+=count
            # print("count:", count)
            # print(ramen)
            
    return answer


N=int(input())
ramen=list(map(int, input().split()))+[0,0]


print(solution(N, ramen))


