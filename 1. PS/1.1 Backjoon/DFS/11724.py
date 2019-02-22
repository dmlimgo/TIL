def dfs(v):
    visit[v] = 1
    # print('in', visit)
    for w in range(1, N+1):
        if arr[v][w] == 1 and visit[w] == 0:
            dfs(w)

import sys
sys.setrecursionlimit(100000)
# sys.stdin=open('11724_input.txt')
N, M = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for m in range(M):
    y, x = map(int, input().split())
    arr[y][x] = 1
    arr[x][y] = 1
cnt = 0
visit = [0] * (N+1)
# print(arr)
for i in range(1, N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
        # print(i, visit, dfs(i))
print(cnt)