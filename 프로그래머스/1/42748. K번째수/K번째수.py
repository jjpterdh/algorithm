def solution(array, commands):
    answer = []
    for command in commands:
        
        slice_arr=array[command[0]-1:command[1]]        
        slice_arr.sort()
        print(slice_arr)
        
        answer.append(slice_arr[command[2]-1])
    return answer