import sys
sys.stdin = open('2925.txt')

def find(char):
    for y in range(R):
        for x in range(C):
            if arr[y][x] == char:
                return x, y

def bfs():
    while q:
        rx, ry, bx, by = q.pop(0)
        for d in range(4):
            nrx = rx + dx[d]
            nry = ry + dy[d]
            nbx = bx + dx[d]
            nby = by + dy[d]
            if arr[nry][nrx] == '#':
                nrx -= dx[d]
                nry -= dy[d]
            if arr[nby][nbx] == '#':
                nbx -= dx[d]
                nby -= dy[d]
            

T = int(input())
for tc in range(T):
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = []
    rx, ry = find(R)
    bx, by = find(B)
    q.append((rx, ry, bx, by))