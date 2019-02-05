T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    print(f'#{tc+1}', end=' ')
    while N % 2 == 0:
        N = N // 2
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N % 3 == 0:
        N = N // 3
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N % 5 == 0:
        N = N // 5
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N % 7 == 0:
        N = N // 7
        cnt += 1
    print(cnt, end=' ')
    cnt = 0
    while N % 11 == 0:
        N = N // 11
        cnt += 1
    print(cnt, end=' ')
    print()