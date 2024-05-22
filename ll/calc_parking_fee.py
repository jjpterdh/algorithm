import math
from collections import deque
def convert_time(time):
    ctime=list(map(int,time.split(":")))
    convert=ctime[0]*60+ctime[1]



    return convert

def solution(fees, records):
    answer = []
    cars={}
    times={}
    total_stay={}
    for record in records:
        time, car, flag=record.split(" ")
        time=convert_time(time)
        if times.get(car) is None:
            times[car]=deque([])
        if cars.get(car) is None:
            cars[car]=0
        if total_stay.get(car) is None:
            total_stay[car]=0

        if flag=="IN":
            times[car].append(time)

        else:
            intime= times[car].popleft()
            stay_time=time-intime
            total_stay[car]+=stay_time
            
            
        
    for key, value in times.items():
        end_time=convert_time("23:59")
        
        if times[key]:
            intime= times[key].popleft()
            stay_time=end_time-intime
            total_stay[key]+=stay_time
    
    for key, value in total_stay.items():
        value-=fees[0]
        if value<=0:
            cars[key]+=fees[1]
        else:
            cars[key]+=fees[1]+(math.ceil(value/fees[2])*fees[3])

    
    for key, value in sorted(cars.items()):

        answer.append(value)
        
    return answer





fees=[180, 5000, 10, 600]
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))