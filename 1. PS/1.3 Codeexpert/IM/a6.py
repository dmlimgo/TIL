n = int(input())
arr = [[0 for _ in range(3)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
for x in range(3):
    for y in range(n):
        done = 0
        if arr[y][x] == 0:
            continue
        for z in range(y+1, n):
            if arr[y][x] == arr[z][x]:
                arr[z][x] = 0
                done = 1
        if done:
            arr[y][x] = 0
for i in range(n):
    print(sum(arr[i]))
