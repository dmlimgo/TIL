import sys
sys.stdin = open('1873.txt')

tank = '< ^ > v'.split()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def find():
    for y in range(H):
        for x in range(W):
            if arr[y][x] in tank:
                for i in range(4):
                    if arr[y][x] == tank[i]:
                        return x, y, i
    return -1, -1, -1

def move(x, y, d):
    newX = x + dx[d]
    newY = y + dy[d]
    if newX < 0 or newY < 0 or newX > W-1 or newY > H-1 or arr[newY][newX] == '*' or arr[newY][newX] == '#' or arr[newY][newX] == '-':
        arr[y][x] = tank[d]
        return x, y, d
    arr[y][x] = '.'
    arr[newY][newX] = tank[d]
    return newX, newY, d

def shoot(x, y, d):
    while True:
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > W - 1 or newY > H - 1 or arr[newY][newX] == '#':
            return
        elif arr[newY][newX] == '*':
            arr[newY][newX] = '.'
            return
        x, y = newX, newY

T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    arr = [[] for _ in range(H)]
    for i in range(H):
        arr[i] = list(input())
    N = int(input())
    command = list(input())
    # for j in range(H):
    #     print(arr[j])
    x, y, d = find()
    for i in range(N):
        if command[i] == 'U':
            x, y, d = move(x, y, 1)
        elif command[i] == 'L':
            x, y, d = move(x, y, 0)
        elif command[i] == 'R':
            x, y, d = move(x, y, 2)
        elif command[i] == 'D':
            x, y, d = move(x, y, 3)
        elif command[i] == 'S':
            shoot(x, y, d)
        # print(i, command[i])
    print('#%d' % (tc+1), end=' ')
    for j in range(H):
        print(''.join(arr[j]))