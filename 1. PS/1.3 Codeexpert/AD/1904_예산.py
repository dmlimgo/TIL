import sys
sys.stdin = open('1904.txt')

def solve(m):
    sum = 0
    for i in range(len(arr)):
        if arr[i] < m: sum += arr[i]
        else: sum += m
    return sum

def bs(s, e, num):
    sol = -1
    while s <= e:
        m = (s + e) // 2
        if solve(m) <= num:
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
ceil = max(arr)
print(bs(0, ceil, M))
