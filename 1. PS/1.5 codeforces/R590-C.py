Q = int(input())
for q in range(Q):
    n = int(input())
    arr = []
    arr.append(list(input()))
    arr.append(list(input()))
    x, y = 0, 0
    d = 0
    pos = 1
    while pos:
        p = arr[y][x]
        if (p == '1') or (p == '2'):
            if d == 0:
                x += 1
            else:
                pos = 0
                break
        else:
            if y == 0:
                if d == 0:
                    y = 1
                    d = 1
                else:
                    x += 1
                    d = 0
            else:
                if d == 0:
                    y = 0
                    d = -1
                else:
                    x += 1
                    d = 0
        if x == n and y == 1:
            pos = 1
            break
        if x > n-1 or y > 1:
            pos = 0
            break
    if pos:
        print('YES')
    else:
        print('NO')
        