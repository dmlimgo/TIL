import sys
sys.stdin = open('3354.txt')

def Qsort(s, e):
    if s >= e: return
    t, p = s, e
    for l in range(s, e):
        if arr[l] > arr[p]:
            arr[l], arr[t] = arr[t], arr[l]
            t += 1
    arr[t], arr[p] = arr[p], arr[t]
    Qsort(s, t-1)
    Qsort(t+1, e)

def Insert(tmp):
    for i in range(len(arr)-1, -1, -1):
        if tmp < arr[i]:
            arr.insert(i+1, tmp)
            return
    arr.insert(0, tmp)

N = int(input())
arr = list(map(int, input().split()))
minval = 10000001

Qsort(0, len(arr)-1)
sum = 0
while len(arr) > 1:
    tmp = arr.pop() + arr.pop()
    sum += tmp
    Insert(tmp)
print(sum)
