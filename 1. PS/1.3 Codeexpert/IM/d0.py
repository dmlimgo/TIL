def move():
    global x, y, d, N, second
    # 현재 장소 스택에 넣기
    newX = x + dx[d]
    newY = y + dy[d]
    # 미래 장소가 벽이거나 자신의 몸이면 리턴
    if newX < 1 or newX > N or newY < 1 or newY > N or area[newY][newX] == 2:
        return -1
    # 이동
    x += dx[d]
    y += dy[d]
    # 현재 장소 스택에 넣기
    snake.append((x, y))
    # 현재 장소 1이 아닐때만
    # 꼬리장소 0으로 만들고 스택에서 빼기
    if area[y][x] != 1:
        tailx, taily = snake[0]
        area[taily][tailx] = 0
        snake.pop(0)
    # 현재 장소 2로 칠하기
    area[y][x] = 2
    # for i in range(N+1):
        # print(area[i])
    # print(second, snake)

N = int(input())
area = [[0 for _ in range(N+1)] for _ in range(N+1)]
K = int(input())
for k in range(K):
    r, c = map(int, input().split())
    area[r][c] = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
d = 2
snake = []
second = 0
L = int(input())
x = y = 1
area[y][x] = 2
snake.append((x, y))
oldt = 0
for l in range(L):
    t, c = input().split()
    t = int(t)
    for i in range(oldt, t):
        second += 1
        result = move()
        if result == -1:
            break
    if result == -1:
        break
    if c == 'D':
        d += 1
        if d > 3:
            d -= 4
    elif c == 'L':
        d -= 1
        if d < 0:
            d += 4
    oldt = t
if result == -1:
    print(second)
else:
# 주어진 조건이 끝나고도 살아있으면
    while True:
        second += 1
        result = move()
        if result == -1:
            print(second)
            break

