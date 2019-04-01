import sys
sys.stdin = open('3357.txt')

def find(arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                return x, y, arr[y][x]
    return -1, -1, -1

def bfs(arr):
    while q:
        x, y, c = q.pop(0)
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 0 or newY < 0 or newX > N-1 or newY > N-1 or arr[newY][newX] != c:
                continue
            q.append((newX, newY, c))
            arr[newY][newX] = 0


N = int(input())
arr = [list(input()) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
narr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            narr[i][j] = 'R'
        else:
            narr[i][j] = arr[i][j]
cnt = 0
while True:
    x, y, c = find(arr)
    if x == -1:
        break
    q = []
    q.append((x, y, c))
    arr[y][x] = 0
    bfs(arr)
    cnt += 1
ccnt = 0
while True:
    x, y, c = find(narr)
    if x == -1:
        break
    q = []
    q.append((x, y, c))
    narr[y][x] = 0
    bfs(narr)
    ccnt += 1
print(cnt, ccnt)
