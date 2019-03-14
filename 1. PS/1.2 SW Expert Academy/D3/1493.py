import sys
sys.stdin = open('1493.txt')

def getval(n):
    s = 1
    i = 1
    while True:
        if s <= n < s + i:
            break
        s += i
        i += 1
    x = 1 + (n - s)
    y = i - (n - s)
    return x, y

def solve(x, y):
    s = 0
    for i in range(1, x+1):
        s += i
    # print(s, i)
    for j in range(1, y):
        s += i + j - 1
        # print(s)
    return s

T = int(input())
for tc in range(T):
    p, q = map(int, input().split())
    x1, y1 = getval(p)
    x2, y2 = getval(q)
    x = x1 + x2
    y = y1 + y2
    print(f'#{tc+1} {solve(x, y)}')