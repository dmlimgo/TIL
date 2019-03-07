import sys
sys.stdin = open('1210.txt')


def findstart():
    for y in range(100):
        for x in range(100):
            if arr[y][x] == 2:
                return x, y

def go(x, y, d):
    while True:
        if d == 0 and (x-1 < 0 or arr[y][x-1] == 0):
            d = 1
        elif d == 1 and y == 0:
            return x
        elif d == 1 and x > 0 and arr[y][x-1] == 1:
            d = 0
        elif d == 1 and x < 99 and arr[y][x+1] == 1:
            d = 2
        elif d == 2 and (x+1 > 99 or arr[y][x+1] == 0):
            d = 1
        x += dx[d]
        y += dy[d]

dx = [-1, 0, 1]
dy = [0, -1, 0]
arr = [[0] for _ in range(100)]
for tc in range(10):
    d = input()
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    x, y = findstart()
    print('#%d %d' % (tc+1, go(x, y, 1)))
