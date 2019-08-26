import sys
sys.stdin = open('2207.txt')

N, M = map(int, input().split())
map_arr = [list(map(int, input())) for _ in range(N)]
visit = [[(1000001, 2) for _ in range(M)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = []
q.append((0, 0 ,1, 0))
visit[0][0] = (1, 0)

def bfs():
    while(q):
        x, y, dis, bomb = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M-1: continue
            if ny < 0 or ny > N-1: continue
            if nx == M-1 and ny == N-1: return dis+1
            if map_arr[ny][nx]: nbomb = bomb + 1
            else: nbomb = bomb
            if nbomb < visit[ny][nx][1]:
                q.append((nx, ny, dis+1, nbomb))
                visit[ny][nx] = (dis+1, nbomb)
    return 0

if (N == 1) and (M == 1): sol = 1
else: sol = bfs()

if sol: print(sol)
else: print(-1)