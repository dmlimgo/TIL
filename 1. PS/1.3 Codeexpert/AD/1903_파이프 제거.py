import sys
sys.stdin = open('1903.txt')

def dfs(x, y):
    for d in possible[arr[y][x]]:
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > N-1:
            continue
        # print(x, y, newX, newY, d, end=' ')
        if d == 0 and 2 in possible[arr[newY][newX]]:
            # print('d=0')
            arr[y][x] = '0'
            dfs(newX, newY)
        elif d == 1 and 3 in possible[arr[newY][newX]]:
            # print('d=1')
            arr[y][x] = '0'
            dfs(newX, newY)
        elif d == 2 and 0 in possible[arr[newY][newX]]:
            # print('d=2')
            arr[y][x] = '0'
            dfs(newX, newY)
        elif d == 3 and 1 in possible[arr[newY][newX]]:
            # print('d=3')
            arr[y][x] = '0'
            dfs(newX, newY)
        arr[y][x] = '0'
        # print('none')


N = int(input())
X, Y = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
possible = {'0':[], '1':[0, 2],'2':[1, 3],'3':[2, 3],
            '4':[0, 3], '5':[0, 1], '6':[1, 2], '7':[1, 2, 3],
            '8':[0, 2, 3], '9':[0, 1, 3], 'A':[0, 1, 2], 'B':[0, 1, 2, 3]}
dfs(X, Y)
cnt = 0
for i in range(N):
    # print(arr[i])
    for j in range(N):
        if arr[i][j] != '0':
            cnt += 1
print(cnt)