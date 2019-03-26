import sys
sys.stdin = open('2275.txt')
import time
start = time.time()
def solve(m):
    global para
    hap = 0
    if para:
        for i in range(N):
            if m >= arr[i]:
                continue
            hap += (arr[i] - m)
    else:
        for i in range(N):
            if m >= arr[i]:
                break
            hap += (arr[i] - m)
    return hap

def bs(s, e):
    global M
    sol = -1
    while s <= e:
        m = (s + e) // 2
        # print(s, m, e, solve(m))
        if solve(m) >= M:
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol

N, M = map(int, input().split())
arr = list(map(int, input().split()))
para = 0
if sum(arr) // 2 <= M:
    arr.sort()
    para = 1
else:
    arr.sort(reverse=True)
# print(arr)
print(bs(0, max(arr)))
print(time.time()-start)