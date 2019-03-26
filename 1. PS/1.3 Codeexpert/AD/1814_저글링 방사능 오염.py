import sys
sys.stdin = open('1814.txt')

def bfs():
    global W, H
    maxval = 3
    while q:
        x, y = q.pop(0)
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 1 or newY < 1 or newX > W or newY > H or arr[newY][newX] != 1:
                continue
            q.append((newX, newY))
            arr[newY][newX] = arr[y][x] + 1
            maxval = arr[newY][newX]
    return maxval

W, H = map(int, input().split())
arr = [[0 for _ in range(W+1)] for _ in range(H+1)]
for i in range(1, H+1):
    arr[i] = [0] + list(map(int, list(input())))
x, y = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = []
q.append((x, y))
arr[y][x] = 3
print(bfs())
cnt = 0
for y in range(H+1):
    for x in range(W+1):
        if arr[y][x] == 1:
            cnt += 1
print(cnt)