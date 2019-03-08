import sys
sys.stdin = open('13460.txt')

def findposition(chr):
    for y in range(N):
        for x in range(M):
            if arr[y][x] == chr:
                return x, y

def iswall(Nrx, Nry):
    global M, N
    if Nrx < 0 or Nry < 0 or Nrx > M - 1 or Nry > N - 1 or arr[Nry][Nrx] == '#':
        return True

def ishole(x, y):
    global gx, gy
    if x == gx and y == gy:
        return True

def solve(x, y):
    for d in range(4):
        Nx = x + dx[d]
        Ny = y + dy[d]
        if iswall(Nx, Ny):
            continue
        x, y = go(x, y, d)
        if x == -1 and y == -1:
            print('solve')
            return
        solve(x, y)

def go(x, y, d):
    while True:
        arr[y][x] = '1'
        nx = x + dx[d]
        ny = y + dy[d]
        if iswall(nx, ny):
            return x, y
        elif ishole(nx, ny):
            success = 1
            return -1, -1
        x, y = nx, ny

N, M = map(int, input().split())
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

rx, ry = findposition('R')
bx, by = findposition('B')
gx, gy = findposition('O')

print(rx, ry)
solve(rx, ry)