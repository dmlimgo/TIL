def paint():
    for y in range(len(r_arr)):
        r = r_arr[y]
        for x in range(r):
            arr[y][x] = 1
        if r < w:
            arr[y][r] = 0
    for x in range(len(c_arr)):
        c = c_arr[x]
        for y in range(c):
            if arr[y][x] == 0:
                return 0
            else:
                arr[y][x] = 1
        if c < h:
            if arr[c][x] == 1:
                return 0
            else:
                arr[c][x] = 0
    return 1

h, w = map(int, input().split())
r_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))

arr = [[2 for _ in range(w)] for _ in range(h)]
pos = paint()
if not pos:
    print(0)
else:
    cnt = 0    
    for y in range(h):
        for x in range(w):
            if arr[y][x] == 2:
                cnt += 1
    print((2**cnt)%1000000007)

    