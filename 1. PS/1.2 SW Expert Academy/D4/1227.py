import sys
sys.stdin = open('1227.txt')

arr = [[0] for _ in range(100)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def findtwo():
    for y in range(100):
        for x in range(100):
            if arr[y][x] == 2:
                return x, y

def go(x, y):
    while True:
        arr[y][x] = 1
        way = 0
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 0 or newY < 0 or newX > 99 or newY > 99 or arr[newY][newX] == 1:
                continue
            elif arr[newY][newX] == 3:
                return 1
            elif arr[newY][newX] == 0:
                way += 1
                dir = d
        if way > 1:
            s.append((x, y))
            x += dx[dir]
            y += dy[dir]
        elif way == 1:
            x += dx[dir]
            y += dy[dir]
        elif s:
            x, y = s.pop()
        elif not s:
            return 0

for tc in range(10):
    d = input()
    for i in range(100):
        arr[i] = list(map(int, list(input())))
    x, y = findtwo()
    s = []
    print('#%d %d' % (tc+1, go(x, y)))
    # for i in range(100):
    #     print(arr[i])