def findone(x, y):
    for b in range(N):
        for a in range(N):
            if arr[b][a] == 1:
                arr[b][a] = 0
                return a, b
    return -1, -1

def shoot(x, y, d):
    cnt = 0
    while True:
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > N-1: return cnt
        if arr[newY][newX] == 0: return cnt
        elif arr[newY][newX] == 1: return cnt
        elif arr[newY][newX] == 2:
            arr[newY][newX] = 3
            cnt += 1
            x, y = newX, newY
        elif arr[newY][newX] == 3:
            x, y = newX, newY

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, list(input())))
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
x = y = 0
kill = 0
while True:
    x, y = findone(x, y)
    if x == -1 and y == -1: break
    for d in range(8):
        kill += shoot(x, y, d)
print(kill)