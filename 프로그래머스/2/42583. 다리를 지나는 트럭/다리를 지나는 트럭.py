
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights=deque(truck_weights)
    
    bridge=deque([0]*bridge_length)
     
    cur_weight=0
    while truck_weights:          
        
        crossed=bridge.popleft()
        
        cur_weight-=crossed
        
        if weight>=cur_weight+truck_weights[0]:
            
            truck=truck_weights.popleft()
            cur_weight+=truck
            bridge.append(truck)
            
        else:
            bridge.append(0)    
        
        # print(bridge, cur_weight)        
        answer+=1

    answer+=bridge_length
    
    return answer