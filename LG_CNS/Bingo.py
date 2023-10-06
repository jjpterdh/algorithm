# Bingo 2578번 백준



def check_garo():
    count=0
    for i in range(5):
        if sum(board[i])>0:
            continue

        count+=1
    
    return count


def check_sero():
    count=0
    
    for i in range(5):
        sum=0
        for j in range(5):
            sum+=board[j][i]
            if sum >0:
                
                break          

        if sum==0:
            count+=1


    return count
    
def check_cross_leftup():
    sum=0
    for i in range(5):
        sum+=board[4-i][i]

    if sum==0:
        return 1

    else:
        return 0




def check_cross_leftdown():
    sum=0
    for i in range(5):

        sum+=board[i][i]
    if sum==0:
        return 1

    else:
        return 0



def check_Bingo(num):
    price=0
    for i in range(5):
        for j in range(5):
            
            if board[i][j]==num:
                board[i][j]=0

                price+=check_garo()
                price+=check_sero()
                price+=check_cross_leftup()
                price+=check_cross_leftdown()

                return price


board=[list(map(int, input().split())) for _ in range(5)]
called=[list(map(int, input().split())) for _ in range(5)]


count=0
flag=False
for i in range(5):

    if flag:
        break

    for j in range(5):
        count+=1
        check=called[i][j]

        bingo=check_Bingo(check)
        
        if bingo >=3:
            flag=True
            break

        bingo=0

print(count)


