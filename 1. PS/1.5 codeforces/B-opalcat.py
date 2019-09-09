import math
t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    m = 987654321
    d = [0] * n
    h = [0] * n
    cnt = -1
    for j in range(n):
        d[j], h[j] = map(int, input().split())
    dmax = max(d)
    if dmax >= x:
        cnt = 1
    else:
        cu = -1
        for j in range(n):
            deal = d[j] - h[j]
            if cu < deal and deal > 0:
                cu = deal
        if cu > 0:
            cnt = math.ceil((x - dmax)/ cu) + 1
        else:
            cnt = -1
    print(cnt)