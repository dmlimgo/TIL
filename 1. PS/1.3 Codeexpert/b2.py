def check(x,y):
    cnt = 0
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]

        if newX < 0 or newY < 0 or newX > 99 or newY > 99 or not arr[newY][newX]:
            cnt += 1

    return cnt
arr = [[0 for _ in range(100)] for _ in range(100)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

paper = int(input())
for n in range(paper):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for i in range(x, x+10):
            arr[j][i] = 1
sum = 0
for y in range(100):
    for x in range(100):
        if arr[y][x]:
            sum += check(x,y)
# for i in range(100):
#     print(arr[i])
print(sum)