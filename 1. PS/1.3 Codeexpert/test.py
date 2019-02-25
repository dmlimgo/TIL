def bingo():
    global bcnt
    for y in range(5):
        print('가로합',sum(arr[y]))
        if sum(arr[y]) == 0:
            bcnt += 1
    for x in range(5):
        vsum = 0
        for y in range(5):
            vsum += arr[y][x]
        print('세로합', vsum)
        if vsum == 0:
            bcnt += 1
    pdiag = 0
    for y in range(5):
        pdiag += arr[y][y]
    print('대각합', pdiag)
    if pdiag == 0:
        bcnt += 1
    ndiag = 0
    for y in range(5):
        ndiag += arr[y][4-y]
    print('대각합', ndiag)
    if ndiag == 0:
        bcnt += 1
arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))
cnt = 0
bcnt = 0
bingo()
