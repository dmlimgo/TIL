import sys
sys.stdin = open('2382.txt')

def bSearch(s, e, num):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] < num:
            s = sol = m + 1
        else:
            e = m - 1
    return sol

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        a = bSearch(j, N-1, arr[j] + 2*(arr[j] - arr[i]) + 1)
        b = bSearch(j, N-1, arr[j] + arr[j] - arr[i])
        cnt += a-b
print(cnt)