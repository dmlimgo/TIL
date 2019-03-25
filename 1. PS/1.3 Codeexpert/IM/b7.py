# 190304 09:12
def find(x, y):
    global total
    short = 10
    for d in range(4):
        dis = 0
        resX, resY = x, y
        while True:
            newX = x + dx[d]
            newY = y + dy[d]
            dis += 1
            if arr[newY][newX] == 0:
                break
            x, y = newX, newY
        if short > dis:
            short = dis
        x, y = resX, resY
    total += short
    return short

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
N = int(input())
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
total = 0
for y in range(N):
    for x in range(N):
        if arr[y][x]:
            arr[y][x] = find(x, y)

print(total)