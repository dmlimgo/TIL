import sys
sys.stdin = open('2542.txt')

def shoot(i, F, R):
    for j in range(N):
        if abs(ship[j][0] - ship[i][0]) + abs(ship[j][1] - ship[i][1]) <= R:
            ship[j][2] -= F


def Rperm(pos, ship):
    global minval
    if pos == M:
        cnt = 0
        for i in ship:
            if i[2] > 0:
                cnt += 1
        if minval > cnt:
            print(ship)
            minval = cnt
        return
    for i in range(N):
        if ship[i][2] > 0:
            shoot(i, F, R)
            Rperm(pos+1, ship)
            shoot(i, -F, R)

# arr = [[0 for _ in range(1000)] for _ in range(1000)]
N = int(input())
ship = []
for i in range(N):
    x, y, e = map(int, input().split())
    ship.append([x, y, e])
    # arr[y][x] = e
M, F, R = map(int, input().split())
minval = 10000001
Rperm(0, ship)
print(minval)