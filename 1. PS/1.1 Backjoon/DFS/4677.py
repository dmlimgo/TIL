def find():
    for y in range(m):
        for x in range(n):
            if arr[y][x] == '@':
                return x, y
    return -1, -1

def solve(x, y):
    global m, n
    arr[y][x] = '*'
    for d in range(8):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > n-1 or newY > m-1 or arr[newY][newX] == '*':
            continue
        solve(newX, newY)

while True:
    m, n = map(int, input().split())
    if m == 0:
        break
    arr = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        arr[i] = list(input())
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [1, 0, -1, -1, -1, 0, 1, 1]
    cnt = 0
    while True:
        x, y = find()
        if x == -1:
            break
        solve(x, y)
        cnt += 1
    print(cnt)
