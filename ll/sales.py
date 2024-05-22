def solution(want, number, discount):
    # 슬라이딩 윈도우?
    answer = 0
    discount_dict={}
    want_dict={}
    for i in range(len(want)):        
        want_dict[want[i]]=number[i]
        discount_dict[want[i]]=0



    for i in range(10):
        if discount_dict.get(discount[i]) is None:
            discount_dict[discount[i]]=0
        discount_dict[discount[i]]+=1

    flag=True
    for i in range(len(want)):
        if want_dict[want[i]]>discount_dict[want[i]]:
            flag=False
            break
    if flag:
        answer+=1

    for i in range(10, len(discount)):
        flag=True
        discount_dict[discount[i-10]]-=1
        if discount_dict.get(discount[i]) is None:
            discount_dict[discount[i]]=0
        discount_dict[discount[i]]+=1

        for i in range(len(want)):
            if want_dict[want[i]]>discount_dict[want[i]]:
                flag=False
                break
        if flag:
            answer+=1
                
    return answer

want=["banana", "apple", "rice", "pork", "pot"]
number=[3, 2, 2, 2, 1]
discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))