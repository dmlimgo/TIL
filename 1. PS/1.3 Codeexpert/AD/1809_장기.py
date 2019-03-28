import sys
sys.stdin = open('1809.txt')
from collections import deque

def bfs():
    while q:
        x, y = q.pop(0)
        if x == zx and y == zy:
            print(visit[y][x]-1)
            return
        for d in range(8):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 1 or newY < 1 or newX > M or newY > N or visit[newY][newX]:
                continue
            visit[newY][newX] = visit[y][x] + 1
            q.append((newX, newY))


N, M = map(int, input().split())
hy, hx, zy, zx = map(int, input().split())
visit = [[0 for _ in range(M+1)] for _ in range(N+1)]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
q = []
q.append((hx, hy))
visit[hy][hx] = 1
bfs()
