# 12:14
import sys
sys.stdin = open('1949.txt')
import copy

def find_big_all():
    maxval = [-1, 0]
    for y in range(N):
        for x in range(N):
            if arr[y][x] > maxval[0]:
                maxval[0] = arr[y][x]
                maxval[1] = [[x, y]]
            elif arr[y][x] == maxval[0]:
                maxval[1].append([x, y])
    return maxval

def dfs(pos, v, nums, dis):
    global maxlen
    x, y = nums
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > N-1 or visit[newY][newX]:
            continue
        if v != 1 and arr[newY][newX] >= arr[y][x]:
            if arr[newY][newX] - K < arr[y][x]:
                tmp = arr[newY][newX]
                arr[newY][newX] = arr[y][x] - 1
                visit[newY][newX] = 1
                dfs(pos+1, 1, [newX, newY], dis+1)
                visit[newY][newX] = 0
                arr[newY][newX] = tmp
        elif arr[newY][newX] < arr[y][x]:
            visit[newY][newX] = 1
            dfs(pos+1, v, [newX, newY], dis+1)
            visit[newY][newX] = 0

    if dis > maxlen:
        maxlen = dis

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    narr = copy.deepcopy(arr)
    maxlen = 0
    maxval = find_big_all()

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(len(maxval[1])):
        visit = [[0 for _ in range(N)] for _ in range(N)]
        visit[maxval[1][i][1]][maxval[1][i][0]] = 1
        dfs(0, 0, maxval[1][i], 1)
    print('#%d %d' % (tc+1, maxlen))
