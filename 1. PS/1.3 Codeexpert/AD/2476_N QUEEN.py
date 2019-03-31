def check(x, y):
    for d in range(4):
        k = 1
        while True:
            newX = x + dx[d] * k
            newY = y + dy[d] * k
            if newX < 0 or newY < 0 or newX > N-1 or newY > N-1:
                break
            elif arr[newY][newX] == 1:
                return False
            k += 1
    return True
def perm(pos):
    global cnt
    if pos == N:
        cnt += 1
        return
    for i in range(N):
        if not visit[i]:
            if check(i, pos):
                visit[i] = 1
                arr[pos][i] = 1
                perm(pos+1)
                arr[pos][i] = 0
                visit[i] = 0

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

dx = [-1, 1, 1, -1]
dy = [-1, -1, 1, 1]
cnt = 0
visit = [0] * N
perm(0)
print(cnt)