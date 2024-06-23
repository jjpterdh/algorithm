def solution(s):
    answer = True
    stack=[]
    for b in s:
        if b=="(":
            stack.append("(")

        else:
            if stack==[]:
                return False
            stack.pop()
                
    if stack:
        return False
    return True

