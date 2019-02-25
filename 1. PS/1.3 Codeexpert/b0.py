def check(call):
    global cnt
    for y in range(5):
        for x in range(5):
            if arr[y][x] == call:
                arr[y][x] = 0
                return

def bingo():
    bcnt = 0
    for y in range(5):
        if sum(arr[y]) == 0:
            bcnt += 1
    for x in range(5):
        vsum = 0
        for y in range(5):
            vsum += arr[y][x]
        if vsum == 0:
            bcnt += 1
    pdiag = 0
    for y in range(5):
        pdiag += arr[y][y]
    if pdiag == 0:
        bcnt += 1
    ndiag = 0
    for y in range(5):
        ndiag += arr[y][4-y]
    if ndiag == 0:
        bcnt += 1
    return bcnt
arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))
cnt = 0
done = 0
for i in range(5):
    call = list(map(int, input().split()))
    for c in range(5):
        check(call[c])
        cnt += 1
        if cnt > 11 and bingo() > 2:
            print(cnt)
            done = 1
            break
    if done:
        break

