import sys
sys.setrecursionlimit(100000)

def start():
    global bk
    for y in range(M):
        for x in range(N):
            if arr[y][x] == 0:
                return x, y
    bk = 1
    return -1, -1

def find(x, y):
    global cnt, tcnt
    cnt += 1
    arr[y][x] = 2
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > M-1 or arr[newY][newX]:
            continue
        find(newX, newY)


M, N, K = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(M)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
tcnt = 0
bk = 0

carr = []
while True:
    x, y = start()
    if bk == 1:
        break
    cnt = 0
    find(x, y)
    carr.append(cnt)
    tcnt += 1
print(tcnt)
carr.sort()
print(' '.join(map(str, carr)))

