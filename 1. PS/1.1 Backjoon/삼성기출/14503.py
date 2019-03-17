# 11:07
import sys
sys.stdin = open('14503.txt')
sys.setrecursionlimit(10000)
def solve(x, y, d):
    global cnt, f
    if arr[y][x] != 2:
        arr[y][x] = 2
        cnt += 1
    for i in range(1, 5):
        nd = (d+i) % 4
        newX = x + dx[nd]
        newY = y + dy[nd]
        if newX < 0 or newY < 0 or newX > M-1 or newY > N-1 or arr[newY][newX]:
            continue
        solve(newX, newY, nd)
    newX = x - dx[d]
    newY = y - dy[d]
    if f:
        return
    if arr[newY][newX] == 1:
        print(cnt)
        f = 1
        return
    else:
        solve(x - dx[d], y - dy[d], d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
f = 0
solve(c, r, 3-d)