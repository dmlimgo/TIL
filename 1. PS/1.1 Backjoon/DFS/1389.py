def bfs(num):
    while s:
        x = s.pop(0)
        for i in range(1, N+1):
            if arr[x][i] and not visit[i]:
                s.append(i)
                visit[i] = visit[x] + 1

N, M = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
s = []
minval = 1000001
minindex = 0
for i in range(1, N+1):
    visit = [0] * (N+1)
    visit[i] = 1
    s.append(i)
    bfs(i)
    if minval > sum(visit):
        minval = sum(visit)
        minindex = i
print(minindex)
