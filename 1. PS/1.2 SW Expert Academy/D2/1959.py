T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    m = 0
    if N > M:
        M, ai, N, bj = N, bj, M, ai
    for i in range(M-N+1):
        hap = 0
        for j in range(N):
            hap += ai[j] * bj[i+j]
        if hap > m:
            m = hap
    print(f'#{tc + 1} {m}')