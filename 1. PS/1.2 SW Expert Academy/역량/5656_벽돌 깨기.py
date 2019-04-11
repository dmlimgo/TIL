import sys
sys.stdin = open('5656.txt')
import copy

def comb(pos, ary):
    if len(ary) == N:
        ball_position.append(ary)
        return
    if pos > W:
        return
    for i in range(W):
        comb(pos+1, ary + [i])

def find_target(ball_pos):
    for y in range(H):
        if arr[y][ball_pos]:
            return ball_pos, y
    return -1, -1

def find_target_all():
    while q:
        x, y = q.pop(0)
        for r in range(arr[y][x]):
            for d in range(4):
                newX = x + dx[d] * r
                newY = y + dy[d] * r
                if newX < 0 or newY < 0 or newX > W-1 or newY > H-1 or arr[newY][newX] == 0 or visited[newY][newX]:
                    continue
                visited[newY][newX] = 1

                q.append((newX, newY))
                targets.append((newX, newY))

def delete_block():
    for target in targets:
        arr[target[1]][target[0]] = 0

def drop_block():
    # 밑에서부터 꼭대기까지 1이 있으면
        # 아래가 마지막이거나 1이면 아무것도 안함
        # 0이라면 아래가 마지막이거나 1일때까지 내려감
    for x in range(W):
        for y in range(H-1, -1, -1):
            if arr[y][x]:
                while (y+1 < H and arr[y+1][x] == 0):
                    tmp = arr[y][x]
                    arr[y][x] = 0
                    arr[y+1][x] = tmp
                    y += 1


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    narr = [list(map(int, input().split())) for _ in range(H)]
    ball_position = []
    comb(0, [])
    minval = 10000001
    for bp in ball_position:
        arr = copy.deepcopy(narr)
        # print('bp',bp)
        for i in range(N):
            visited = [[0 for _ in range(W)] for _ in range(H)]
            targets = []
            x, y = find_target(bp[i])
            # print('xy', x, y)
            if x != -1:
                q = []
                visited[y][x] = 1
                q.append((x, y))
                targets.append((x, y))
                find_target_all()
                delete_block()
                drop_block()

        cnt = 0
        for y in range(H):
            # print(arr[y])
            for x in range(W):
                if arr[y][x]:
                    cnt += 1
        # print(cnt)
        if cnt < minval:
            minval = cnt
    if minval == 10000001:
        print('#%d %d' % (tc+1, 0))
    else:
        print('#%d %d' % (tc + 1, minval))
