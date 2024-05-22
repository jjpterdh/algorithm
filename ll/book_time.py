import heapq

def convert_time(book_time):
    converted_time=[]

    for time in book_time:
        s=time[0]
        e=time[1]
            
        sh,sm=map(int, s.split(":"))
        start_time=sh*60+sm
        eh,em=map(int, e.split(":"))
        end_time=eh*60+em
        converted_time.append((start_time, end_time))

    return converted_time

def solution(book_time):
    heap=[]
    answer = 1
    book_time=convert_time(book_time)
    book_time.sort()


    for i in range(len(book_time)):
        if not heap:
            heapq.heappush(heap, book_time[i][1])
            continue
        if book_time[i][0]<heap[0]+10: # 시작 시간이 끝나는 시간보다 빠름
            answer+=1
        else:
            heapq.heappop(heap)
        heapq.heappush(heap, book_time[i][1])
    return answer


book_time=[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))