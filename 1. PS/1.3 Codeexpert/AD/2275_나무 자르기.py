import sys
sys.stdin = open('2275.txt')
import time
start = time.time()
def solve(m):
    hap = 0
    for i in range(N):
        if m < arr[i]:
            hap += (arr[i] - m)
    # for i in range(N):
    #     if m >= arr[i]:
    #         break
    #     hap += (arr[i] - m)
    # print('func', end=' ')
    # j = len(arr)
    # for i in range(N):
    #     if m >= arr[i]:
    #         j = i
    #         break
    # print(j, m, sum(arr[:j]), m*j)
    # hap = sum(arr[:j]) - m*j
    return hap

def bs(s, e):
    global M
    sol = -1
    while s <= e:
        m = (s + e) // 2
        hap = solve(m)
        # print(s, m, e, hap)
        # print(time.time() - start)
        # if hap == M:
        #     return m
        # elif hap > M:
        #     sol = m
        #     s = m + 1
        if hap >= M:
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# print(time.time()-start)
# print(arr)
print(bs(0, max(arr)))
print(time.time()-start)