import sys
sys.stdin = open('1858.txt')

def bfs():
    while q:
        x, y = q.pop(0)
        for d in range(4):
            newX = x + dx[d]
            newY = y + dy[d]
            if newX < 0 or newY < 0 or newX > N-1 or newY > N-1:
                continue
            newhap = memo[y][x] + arr[newY][newX]
            if memo[newY][newX] > newhap:
                memo[newY][newX] = newhap
                q.append((newX, newY))


N = int(input())
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, list(input())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
memo = [[10000001 for _ in range(N)] for _ in range(N)]
done = 0
q = []
q.append((0, 0))
memo[0][0] = arr[0][0]
bfs()
print(memo[N-1][N-1])