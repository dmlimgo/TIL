def iswall(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1 or arr[y][x] == 1:
        return 1
    elif arr[y][x] == 2:
        return -1
def go(x, y):
    d = dis = 0
    while True:
        cnt = 0
        while True:
            newX = x + ndx[d]
            newY = y + ndy[d]
            if iswall(newX, newY) == 1:
                d += 1
                cnt += 1
                if d > 3:
                    d %= 4
            elif iswall(newX, newY) == -1:
                return dis
            else:
                break
            if cnt == 4:
                return dis
        x += ndx[d]
        y += ndy[d]
        arr[y][x] = 2
        dis += 1

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, list(input())))
info = list(map(int, input().split()))
dx = [0, 0, -1, 0, 1]
dy = [0, 1, 0, -1, 0]
ndx = []
ndy = []
for i in info:
    ndx.append(dx[i])
    ndy.append(dy[i])
x = y = 0
d = 0
print(go(x, y))