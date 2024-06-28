import math
import sys


sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m


def make_seg(idx, s, e):
    if s == e:
        seg[idx] = arr[s]
        return seg[idx]

    mid = (s + e) // 2
    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)
    seg[idx] = l + r
    return seg[idx]


def change(idx, s, e):
    if s == e:
        seg[idx] = b
        return

    seg[idx] += diff
    mid = (s + e) // 2
    if s <= a <= mid:
        change(idx * 2, s, mid)
    else:
        change(idx * 2 + 1, mid + 1, e)


def get(idx, s, e):
    if y < s or e < x:
        return 0

    if x <= s and e <= y:
        return seg[idx]
    else:
        mid = (s + e) // 2
        l = get(idx * 2, s, mid)
        r = get(idx * 2 + 1, mid + 1, e)
        return l + r


n, q = map(int, input().split())
arr = list(map(int, input().split()))

b = math.ceil(math.log2(n)) + 1
node_n = 1 << b
seg = [0 for _ in range(node_n)]

make_seg(1, 0, n - 1)

for i in range(q):
    x, y, a, b = map(int, input().split())
    x, y, a = x - 1, y - 1, a - 1
    if x > y:
        x, y = y, x
    diff = b - arr[a]
    arr[a] = b
    print(get(1, 0, n - 1))
    change(1, 0, n - 1)