import sys
sys.stdin = open('1803.txt')

def find_apart():
    global N
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                return x, y
    return -1, -1

def dfs(x, y):
    global cnt, N
    cnt += 1
    arr[y][x] = 0
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > N-1 or arr[newY][newX] == 0:
            continue
        dfs(newX, newY)

N = int(input())
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, list(input())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

counts = []
while True:
    x, y = find_apart()
    if x == -1:
        break
    cnt = 0
    dfs(x, y)
    counts.append(cnt)
counts.sort()
print(len(counts))
for i in range(len(counts)):
    print(counts[i])