def iswall(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1 or arr[y][x] == 1:
        return 1
    elif arr[y][x] == 2:
        return -1

def go(x, y, d, cnt, dis):
    newX = x + ndx[d]
    newY = y + ndy[d]
    if cnt == 4:
        print(dis)
        return
    if iswall(newX, newY) == 1:
        go(x, y, (d+1) % 4, cnt+1, dis)
    elif iswall(newX, newY) == -1:
        print(dis)
        return
    else:
        arr[y][x] = 2
        go(newX, newY, d, 0, dis+1)


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
cnt = 0
dis = 0
go(x, y, d, cnt, dis)
