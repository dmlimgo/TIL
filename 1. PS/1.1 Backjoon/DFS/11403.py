def dfs(v):
    global N, n
    n += 1
    if n != 1:
        visit[v] = 1
    for w in range(1, N+1):
        if arr[v][w] == 1 and visit[w] == 0:
            dfs(w)


N = int(input())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for n in range(1, N+1):
    arr[n][1:] = list(map(int, input().split()))
for i in range(1, N+1):
    visit = [0 for _ in range(N + 1)]
    n = 0
    dfs(i)
    print(visit[1:])
