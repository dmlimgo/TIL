def dfs(pos, arr):
    if pos == 3:
        for i in range(3):
            print(arr[i], end=' ')
        print()
        return
    dfs(pos+1, arr + [pos+1])
    dfs(pos+1, arr + [0])
dfs(0, [])