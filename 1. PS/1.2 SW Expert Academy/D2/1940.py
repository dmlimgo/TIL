T = int(input())
for tc in range(T):
    N = int(input())
    s = 0
    d = 0
    for n in range(N):
        c = list(map(int, input().split()))
        if len(c) > 1:
            c, a = c[0], c[1]
        else:
            c = c[0]
        if c == 0:
            d += s
        elif c == 1:
            s += a
            d += s
        elif c == 2:
            s -= a
            if s < 1:
                s = 0
            d += s
    print(f'#{tc+1} {d}')