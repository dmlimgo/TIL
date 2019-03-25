import sys
sys.stdin = open('c5.txt')

def result():
    global kmin, kmax
    minVal = 10000001
    for i in range(len(arr_dict) - 2):
        for j in range(i + 1, len(arr_dict) - 1):
            c = sum(list(arr_dict.values())[:i + 1])
            b = sum(list(arr_dict.values())[i + 1:j + 1])
            a = sum(list(arr_dict.values())[j + 1:])
            if min(a, b, c) < kmin:
                continue
            if max(a, b, c) > kmax:
                continue
            dif = max(a, b, c) - min(a, b, c)
            if dif < minVal:
                minVal = dif
    if minVal == 10000001:
        return -1
    else:
        return minVal


T = int(input())
for tc in range(T):
    N, kmin, kmax = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr_dict = {}
    for i in arr:
        if i not in arr_dict:
            arr_dict[i] = 1
        else:
            arr_dict[i] += 1
    print(result())
