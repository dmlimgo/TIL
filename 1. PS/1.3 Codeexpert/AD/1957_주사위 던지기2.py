def dfs(pos, hap, arr):
    global N, M
    # print(pos, hap, arr)
    if pos == N:
        if hap == M:
            for i in range(N):
                print(arr[i], end=' ')
            print()
        return
    for i in range(1, 7):
        dfs(pos+1, hap+i, arr + [i])

N, M = map(int, input().split())
dfs(0, 0, [])