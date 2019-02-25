n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x = y = d = 0
for i in range(n**2):
    arr[y][x] = i+1
    newX = x + dx[d]
    newY = y + dy[d]
    if newX < 0 or newX > n-1 or newY < 0 or newY > n-1 or arr[newY][newX]:
        d += 1
    if d > 3:
        d %= 4
    x += dx[d]
    y += dy[d]
for i in range(n):
    print(' '.join(map(str, arr[i])))