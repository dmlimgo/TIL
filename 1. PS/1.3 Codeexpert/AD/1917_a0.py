def Qsort(s, e):
    if s >= e: return
    t, p = s, e
    for l in range(s, e):
        if arr[l] > arr[p]:
            arr[l], arr[t] = arr[t], arr[l]
            t += 1
    arr[p], arr[t] = arr[t], arr[p]
    Qsort(s, t-1)
    Qsort(t+1, e)

N = int(input())
arr = list(map(int, input().split()))
Qsort(0, N-1)
print(' '.join(map(str, arr)))