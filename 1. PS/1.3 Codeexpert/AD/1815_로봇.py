import sys
sys.stdin = open('1815.txt')

def bfs():
    dis_cnt = 0
    while q:
        x, y, d = q.pop(0)
        print(x, y, d, dis_cnt)
        if x == gx and y == gy:
            continue
        for nd in range(1, 5):
            newX = x + dx[nd]
            newY = y + dy[nd]
            if newX < 0 or newY < 0 or newX > N-1 or newY > M-1 or arr[newY][newX] == 1:
                continue
            if nd != d:
                if memo[newY][newX] > memo[y][x] + 2:
                    if newX == gx and newY == gy:
                        if nd != gd:
                            memo[newY][newX] = memo[y][x] + 3
                        else:
                            memo[newY][newX] = memo[y][x] + 2
                    else:
                        memo[newY][newX] = memo[y][x] + 2
                    dis_cnt = 1
                    q.append((newX, newY, nd))
            else:
                if memo[newY][newX] > memo[y][x]:
                    if x == sx and y == sy:
                        if newX == gx and newY == gy:
                            if nd != gd:
                                memo[newY][newX] = memo[y][x] + 1
                            else:
                                memo[newY][newX] = memo[y][x]
                        else:
                            dis_cnt += 1
                            memo[newY][newX] = memo[y][x] + 1
                    else:
                        dis_cnt += 1
                        if dis_cnt > 3 and dis_cnt % 3 == 1:
                            if newX == gx and newY == gy:
                                if nd != gd:
                                    memo[newY][newX] = memo[y][x] + 2
                                else:
                                    memo[newY][newX] = memo[y][x] + 1
                            else:
                                memo[newY][newX] = memo[y][x] + 1
                        else:
                            if newX == gx and newY == gy:
                                if nd != gd:
                                    memo[newY][newX] = memo[y][x] + 1
                                else:
                                    memo[newY][newX] = memo[y][x]
                            else:
                                memo[newY][newX] = memo[y][x]
                    q.append((newX, newY, nd))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
sy, sx, sd = map(int, input().split())
gy, gx, gd = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
memo = [[1000001 for _ in range(N)] for _ in range(M)]
q = []
q.append((sx, sy, sd))
memo[sy][sx] = 0
# for i in range(M):
#     print(memo[i])
bfs()
for y in range(M):
    for x in range(N):
        if memo[y][x] == 1000001:
            memo[y][x] = 0
for i in range(M):
    print(memo[i])
print(memo[gy][gx])