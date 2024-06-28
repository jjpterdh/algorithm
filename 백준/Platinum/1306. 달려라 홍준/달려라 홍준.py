seg = [0 for _ in range(4040404)]
 
def init(n,s,e):
    if s == e:
        seg[n] = a[s-1]
        return seg[n]
    mid = (s+e)//2
    seg[n] = max( init(n*2,s,mid), init(n*2+1,mid+1,e) )
    return seg[n]
 
def getMax(n,l,r,s,e):
    if e < l or r < s: return 0
    if l <= s and e <= r: return seg[n]
    mid = (s+e)//2
    return max( getMax(n*2,l,r,s,mid), getMax(n*2+1,l,r,mid+1,e) )
 
n, m = map(int, input().split())
p = m*2-1 # 시야범위
a = list(map(int, input().split()))
ans = []
 
init(1,1,n)
 
for i in range(n-p+1):
    ans.append(getMax(1,1+i,i+p,1,n))
print(*ans)
