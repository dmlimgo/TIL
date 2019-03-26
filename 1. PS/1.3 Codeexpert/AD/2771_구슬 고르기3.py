def dfs(pos, arr):
    if pos == 3:
        for i in range(3):
            print(arr[i]+1, end=' ')
        print()
        return
    for i in range(3):
        if not visit[i]:
            visit[i] = 1
            dfs(pos+1, arr + [i])
            visit[i] = 0

visit = [0, 0, 0]
dfs(0, [])