def find(x, parent):
    if parent[x]!=x:
        parent[x]=find(parent[x], parent)
    
    return parent[x]
    

def union(a,b, parent):
    a=find(a, parent)
    b=find(b, parent)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

    

def solution(cards):
    parent=[i for i in range(len(cards)+1)]
    answer = 0
    cards=[0]+cards
    
    for i in range(1, len(cards)):
        if parent[i]==i:
            idx=cards[i]
            while idx!=i:
                union(i, idx, parent)
                idx=cards[idx]
            # union(i, cards[i], parent)
        
    
    counts=[0]*(len(cards))
    for i in range(1, len(cards)):
        counts[parent[i]]+=1
    counts.sort(reverse=True)

    if counts[0]==len(cards):
        answer=0
    else:
        answer=counts[0]*counts[1]



    return answer



cards=[8,6,3,7,2,5,1,4]
print(solution(cards))