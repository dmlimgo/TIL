import sys
sys.stdin = open('3351.txt')

def find(n):
    for y in range(N):
        for x in range(M):
            if arr[y][x] == n:
                return x, y
    return -1, -1

def bfs():
    while q:
        x, y = q.pop(0)
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 0 or newY < 0 or newX > M-1 or newY > N-1 or arr[newY][newX]:
                continue
            arr[newY][newX] = arr[y][x] + 1
            q.append((newX, newY))
    return arr[y][x]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = []
while True:
    x, y = find(1)
    if x == -1:
        break
    arr[y][x] = 2
    q.append((x, y))

result = bfs()
x, y = find(0)
if x != -1:
    print(-1)
else:
    print(result-2)

