n, a, x, b, y = map(int, input().split())
while True:
    if a == b:
        print('YES')
        break
    if a == x or b == y:
        print('NO')
        break
    a += 1
    b -= 1
    if a > n:
        a = 1
    if b < 1:
        b = n