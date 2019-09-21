N = int(input())
arr = [['W' for _ in range(N)]for _ in range(N)]
for y in range(N):
    for x in range(N):
        if (x+y) % 2 == 0:
            print(x,y,'W')
            arr[y][x] = 'W'
        else:
            print(x,y,'B')
            arr[y][x] = 'B'
for i in range(N):
    print(''.join(arr[i]))