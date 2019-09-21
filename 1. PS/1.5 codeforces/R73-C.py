Q = int(input())
for q in range(Q):
    c, m, x = map(int, input().split())
    if c == 0 or m == 0:
        print(0)
        continue
    if min(c,m,x) == x:
        c -= x
        m -= x
        b = max(c, m)
        s = min(c, m)
        if (s+b)//3 > s:
            print(s+x)
        else:
            print((s+b)//3+x)
        continue
    if min(c,m,x) == c or min(c,m,x) == m:
        print(min(c,m,x))
        continue
