from collections import deque


def solution(prices):
    answer = []
    prices=deque(prices)
    
    while prices:
        price=prices.popleft()
        cnt=0
        for after in prices:
            # print(price, after)
            cnt+=1
            if after<price:                
                break
        answer.append(cnt)
    
    return answer
