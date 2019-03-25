import sys
sys.stdin = open('2319.txt')

def lowsearch(s, e, num):
    low = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] == num:
            low = m
            e = m - 1
        elif arr[m] >= num:
            e = m - 1
        else:
            s = m + 1
    return low

def highsearch(s, e, num):
    high = -1
    while s <= e:
        m = (s + e) // 2
        if arr[m] == num:
            high = m
            s = m + 1
        elif arr[m] >= num:
            e = m - 1
        else:
            s = m + 1
    return high

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

for i in range(M):
    low = lowsearch(0, N-1, nums[i])
    high = highsearch(0, N-1, nums[i])
    # print(low, high, nums[i])
    if low == -1:
        print(0, end=' ')
    else:
        print(high-low+1, end=' ')
