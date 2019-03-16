# 10:40
import sys
import copy
sys.stdin = open('14502.txt')
sys.setrecursionlimit(100000)

def find_virus():
    for y in range(N):
        for x in range(M):
            if narr[y][x] == 2:
                return x, y
    return -1, -1

def infect(x, y):
    global N, M
    narr[y][x] = 3
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > M - 1 or newY > N - 1 or narr[newY][newX] == 1 or narr[newY][newX] == 3:
            continue
        infect(newX, newY)

def safe_area():
    cnt = 0
    for y in range(N):
        for x in range(M):
            if narr[y][x] == 0:
                cnt += 1
    return cnt


def dfs(wall):
    global N, M, maxval, arr, narr
    if wall == 3:
        narr = copy.deepcopy(arr)
        safe = 0
        while True:
            x, y = find_virus()
            if x == -1:
                break
            infect(x, y)
        safe = safe_area()
        if safe > maxval:
            maxval = safe
        return
    else:
        for y in range(N):
            for x in range(M):
                if arr[y][x] == 0:
                    arr[y][x] = 1
                    dfs(wall + 1)
                    arr[y][x] = 0


N, M = map(int, input().split())
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
maxval = 0
dfs(0)
# print(N, M)
# for i in range(N):
#     print(arr[i])
print(maxval)