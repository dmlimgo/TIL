import sys
sys.stdin = open('1953.txt')

def bfs():
    global cnt
    while q:
        x, y = q.pop(0)
        for d in pipe[arr[y][x]]:
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 0 or newY < 0 or newX > M-1 or newY > N-1 or arr[newY][newX] == 0 or visit[newY][newX]:
                continue
            if (d == 0 and 2 in pipe[arr[newY][newX]]) or (d == 1 and 3 in pipe[arr[newY][newX]]) or (d == 2 and 0 in pipe[arr[newY][newX]]) or (d == 3 and 1 in pipe[arr[newY][newX]]):
                if visit[y][x] + 1 <= L:
                    visit[newY][newX] = visit[y][x] + 1
                    q.append((newX, newY))
                    cnt += 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
pipe = {1:[0, 1, 2, 3], 2:[1, 3], 3:[0, 2],
        4:[1, 2], 5:[2, 3], 6:[0, 3], 7:[0, 1]}

T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = []
    visit[R][C] = 1
    q.append((C, R))
    cnt = 0
    bfs()
    print('#%d %d' % (tc+1, cnt+1))