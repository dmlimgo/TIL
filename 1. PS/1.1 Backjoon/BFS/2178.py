import sys
sys.stdin = open('2178.txt')

def bfs():
    global N, M, minval
    while s:
        x, y, dis = s.pop(0)
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 0 or newY < 0 or newX > M-1 or newY > N-1 or arr[newY][newX] == 0:
                continue
            if newX == M-1 and newY == N-1:
                if minval > dis:
                    minval = dis
                return
            s.append((newX, newY, dis+1))
            arr[newY][newX] = 0
    return minval
N, M = map(int, input().split())
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, list(input())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

s = []
dis = 0
minval = 10000001
s.append((0, 0, 1))
arr[0][0] = 0
bfs()
print(minval+1)