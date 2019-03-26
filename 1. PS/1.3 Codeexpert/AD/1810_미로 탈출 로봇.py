import sys
sys.stdin = open('1810.txt')

def bfs():
    global gx, gy
    while q:
        x, y = q.pop(0)
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 1 or newY < 1 or newX > X or newY > Y or arr[newY][newX]:
                continue
            if newX == gx and newY == gy:
                print(arr[y][x])
                return
            q.append((newX, newY))
            arr[newY][newX] = arr[y][x] + 1



X, Y = map(int, input().split())
arr = [[0 for _ in range(X+1)] for _ in range(101)]
sx, sy, gx, gy = map(int, input().split())
for i in range(1, Y+1):
    arr[i] = [0] + list(map(int, list(input())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = []
q.append((sx, sy))
arr[sy][sx] = 1
bfs()