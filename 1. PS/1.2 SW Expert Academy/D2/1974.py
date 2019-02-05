T = int(input())
for tc in range(T):
    arr = [[0 for _ in range(9)] for _ in range(9)]
    res = 1
    for i in range(9):
        arr[i] = list(map(int, input().split()))
    for y in range(9):
        if sum(arr[y]) != 45:
            res = 0
    for x in range(9):
        hap = 0
        for y in range(9):
            hap += arr[y][x]
        if hap != 45:
            res = 0
    for y in range(0,9,3):
        for x in range(0,9,3):
            hap = 0
            hap += sum(arr[y][x:x + 3])
            hap += sum(arr[y + 1][x:x + 3])
            hap += sum(arr[y + 2][x:x + 3])
            if hap != 45:
                res = 0
    if res:
        print(f'#{tc + 1} {1}')
    else:
        print(f'#{tc + 1} {0}')
