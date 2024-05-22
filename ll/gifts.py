def count_gifts(friends, kakao, received):
    count={}
    
    for f in friends:
        count[f]=0

    print(kakao)

    for f1 in friends:
        for f2 in friends:
            if f1==f2:
                continue
                
            if kakao[f1].get(f2) is None and kakao[f2].get(f1) is None: # 서로 선물을 주고 받은 적이 없음
                # 선물 지수 비교 (준 선물의 수 - 받은 선물의 수)
            
                send_gifts_f1=sum(kakao[f1].values())
                receive_gifts_f1=received[f1]
                point_f1=send_gifts_f1-receive_gifts_f1

                send_gifts_f2=sum(kakao[f2].values())
                receive_gifts_f2=received[f2]
                point_f2=send_gifts_f2-receive_gifts_f2

                if point_f1>point_f2:
                    count[f1]+=1
                elif point_f1<point_f2:
                    count[f2]+=1

            elif kakao[f1].get(f2) is None:
                #f2 만 선물
                count[f2]+=1
            elif kakao[f2].get(f1) is None:
                #f1 만 선물
                count[f1]+=1

            else:
                
                if kakao[f1][f2]==kakao[f2][f1]: # 보낸 선물 개수가 동일
                    
                    # 선물 지수 비교 (준 선물의 수 - 받은 선물의 수)
                    send_gifts_f1=sum(kakao[f1].values())
                    receive_gifts_f1=received[f1]
                    point_f1=send_gifts_f1-receive_gifts_f1

                    send_gifts_f2=sum(kakao[f2].values())
                    receive_gifts_f2=received[f2]
                    point_f2=send_gifts_f2-receive_gifts_f2

                    if point_f1>point_f2:
                        count[f1]+=1
                    elif point_f1<point_f2:
                        count[f2]+=1

                else: 
                    if kakao[f1][f2]>kakao[f2][f1]:
                        count[f1]+=1
                    else:
                        count[f2]+=1

    return count

def solution(friends, gifts):
    
    kakao={}
    received={}

    for f in friends:
        kakao[f]=dict()
        received[f]=0
    
    for gift in gifts:
        a,b=gift.split()
        if kakao[a].get(b) is None:
            kakao[a][b]=1
        
        else:
            kakao[a][b]+=1
        
        received[b]+=1
        
        
    
    count=count_gifts(friends, kakao, received)
        
        
    print(count)
    answer = max(count.values())
    return answer

friends=["muzi", "ryan", "frodo", "neo"]
gifts=["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]



print(solution(friends, gifts))