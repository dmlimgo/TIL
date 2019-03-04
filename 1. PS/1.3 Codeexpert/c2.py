def findtwo():
    for y in range(H):
        for x in range(W):
            if arr[y][x] == 2:
                return x, y

def go(x, y, d, cnt):
    if d == N:
        print(cnt)
        return
    arr[y][x] = 2
    newX = x + ndx[d]
    newY = y + ndy[d]
    if newX < 0 or newY < 0 or newX > W-1 or newY > H-1 or arr[newY][newX] == 1:
        go(x, y, d+1, cnt)
    elif arr[newY][newX] == 2:
        go(newX, newY, d, cnt)
    else:
        go(newX, newY, d, cnt+1)

W, H = map(int, input().split())
arr = [0 for _ in range(H)]
for h in range(H):
    arr[h] = list(map(int, list(input())))
N = int(input())
info = list(map(int, input().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
ndx = []
ndy = []
for i in info:
    ndx.append(dx[i])
    ndy.append(dy[i])
x, y = findtwo()
go(x, y, 0, 1)
# for h in range(H):
#     print(arr[h])