def change_num(num, k):
    new_num=[]
    while num>0:
        new_num.append(num%k)
        num//=k
        if num<k:
            new_num.append(num)
            break
    return new_num[::-1]

def check_prime(num):
    if num==1:
        return False
    for i in range(2,int(num**(0.5))+1):
        if num%i==0:
            return False

    return True

def solution(n, k):
    answer = -1
    arr=change_num(n,k)
    prime=0
    cnt=0
    for i in range(len(arr)):
        if arr[i]!=0:
            prime+=arr[i]
            prime*=10

        else:
            if prime!=0:
                prime//=10
                if check_prime(prime):
                    # print(prime)
                    cnt+=1
            prime=0
    if prime!=0:
                prime//=10
                if check_prime(prime):
                    # print(prime)
                    cnt+=1
    answer=cnt
    return answer



n=437674
k=3
print(solution(n,k))