T = int(input())
for tc in range(T):
    n, a, b = map(int, input().split())
    m = (a + b) * n
    for r in range(1, n+1):
        for c in range(1, int(n/r)+1):
            s = a * abs(r - c) + b * (n - r * c)
            if s < m:
                m = s
    print(f'#{tc+1} {m}')

