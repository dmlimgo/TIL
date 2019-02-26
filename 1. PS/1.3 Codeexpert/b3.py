N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, list(input())))
domore = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max = 0
# n = 0
while domore:
    check = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                cnt = 0
                min = arr[y][x-1]
                for d in range(4):
                    newX = x + dx[d]
                    newY = y + dy[d]
                    if newX < 0 or newY < 0 or newX > N-1 or newY > N-1:
                        continue
                    if arr[newY][newX]:
                        cnt += 1
                if cnt == 4:
                    for d in range(4):
                        newX = x + dx[d]
                        newY = y + dy[d]
                        if arr[newY][newX] < min:
                            min = arr[newY][newX]

                    if arr[y][x] != min + 1:
                        arr[y][x] = min + 1
                        check = 1
                if arr[y][x] > max:
                    max = arr[y][x]
    # print(check)
    if check == 0:
        domore = 0

    # n += 1
    # print(n)
    # for i in range(N):
    #     print(arr[i])
    # if n == 4:
    #     break
    # print()

print(max)