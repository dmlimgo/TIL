# 11:55
import sys
sys.stdin = open('16234.txt')

def search():
    for y in range(N):
        for x in range(N):
            if not visit[y][x]:
                return x, y
    return -1, -1

def dfs(x, y):
    global hap, cnt
    visit[y][x] = 1
    cnt += 1
    hap += arr[y][x]
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > N-1 or visit[newY][newX]:
            continue
        elif L <= abs(arr[newY][newX]-arr[y][x]) <= R:
            dfs(newX, newY)

def change(num):
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 1:
                arr[y][x] = num
                visit[y][x] = 2

N, L, R = map(int, input().split())
arr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
visit = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0 ,1, 0]
dy = [0, -1, 0, 1]
move = 0
flag = 0
while True:
    print('start')
    for i in range(N):
        print(arr[i])
    x, y = search()
    print(x, y, 'search')
    if x == -1:
        if flag == 1:
            move += 1
            visit = [[0 for _ in range(N)] for _ in range(N)]
            flag = 0
            continue
        elif flag == 0:
            break
    hap = 0
    cnt = 0
    dfs(x, y)
    if cnt > 1:
        flag = 1
        change(hap//cnt)
    print('end',x,y,move, cnt, flag)
    for i in range(N):
        print(arr[i])
print(move)