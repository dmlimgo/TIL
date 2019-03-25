def uppersearch(s, e, data):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if data == Narr[m]:
            s = m+1
            sol = m
        elif data > Narr[m]:
            s = m+1
        else:
            e = m - 1
    return sol

N = int(input())
Narr = list(map(int, input().split()))
T = int(input())
Tarr = list(map(int, input().split()))

for i in range(T):
    lo = lowersearch(0, N-1, Tarr[i])
    if lo >= 0:
        up = uppersearch(0, N-1, Tarr[i])
