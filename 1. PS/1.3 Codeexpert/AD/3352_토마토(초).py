import sys
sys.stdin = open('3352.txt')

def find(n):
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if arr[z][y][x] == n:
                    return x, y, z
    return -1, -1, -1

def bfs():
    while q:
        x, y, z = q.pop(0)
        for d in range(6):
            newX = x + dx[d]
            newY = y + dy[d]
            newZ = z + dz[d]
            if newX < 0 or newY < 0 or newZ < 0 or newX > M-1 or newY > N-1 or newZ > H-1 or arr[newZ][newY][newX]:
                continue
            arr[newZ][newY][newX] = arr[z][y][x] + 1
            q.append((newX, newY, newZ))
    return arr[z][y][x]

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = []
while True:
    x, y, z = find(1)
    if x == -1:
        break
    arr[z][y][x] = 2
    q.append((x, y, z))

result = bfs()
x, y, z= find(0)
if x != -1:
    print(-1)
else:
    print(result-2)

