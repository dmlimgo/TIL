T = int(input())
for tc in range(T):
    print(f'#{tc + 1}')
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            print(arr[N-j-1][i], end='')
        print(end=' ')
        for j in range(N):
            print(arr[N-i-1][N-j-1], end='')
        print(end=' ')
        for j in range(N):
            print(arr[j][N-i-1], end='')
        print()
