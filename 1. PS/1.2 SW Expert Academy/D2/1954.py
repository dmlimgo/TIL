T = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for tc in range(T):
    N = int(input())
    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
    x = y = 0
    nx = ny = 0
    idx = 0
    for i in range(1, N**2+1):
        x, y = nx, ny
        arr[y][x] = i
        nx = x + dx[idx]
        ny = y + dy[idx]
        if arr[ny][nx] or nx > N-1 or ny > N-1 or nx < 0 or ny < 0:
            idx = (idx + 1) % 4
            nx = x + dx[idx]
            ny = y + dy[idx]
    print(f'#{tc + 1}')
    for i in range(N):
        print(' '.join(map(str, arr[i][0:N])))