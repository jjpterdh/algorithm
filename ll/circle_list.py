def solution(elements):
    
    length=len(elements)
    elements*=2
    table=set()
    for l in range(1, length+1):
        
        for i in range(length):

            table.add(sum(elements[i:(i+l)]))

        
    return len(table)



elements=[7,9,1,1,4]
print(solution(elements))