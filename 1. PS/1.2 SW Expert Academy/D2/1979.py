import sys
sys.stdin = open('1979_input.txt')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(1, N+1):
        arr[i][1:-1] = list(map(int, input().split()))
    find_list = list(map(int, ('0 ' + '1 '*K + '0').split()))
    cnt = 0
    for y in range(1, N+1):
        for x in range(N-K+1):
            if arr[y][x:x+K+2] == find_list:
                cnt += 1
    arr_t = [[0 for _ in range(N+2)] for _ in range(N+2)]
    for x in range(1, N+1):
        for y in range(1, N+1):
            arr_t[y][x] = arr[x][y]
    for y in range(1, N+1):
        for x in range(N-K+1):
            if arr_t[y][x:x+K+2] == find_list:
                cnt += 1
    print(f'#{tc+1} {cnt}')
