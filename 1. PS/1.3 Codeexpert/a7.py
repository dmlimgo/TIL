import copy

def rotate():
    global n
    for y in range(n):
        for x in range(n):
            arr[y][x] = narr[n-x-1][y]


n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

while True:
    degree = int(input())
    if degree == 0:
        break

    elif degree == 90 or degree == 180 or degree == 270 or degree == 360:
        for r in range(degree//90):
            narr = copy.deepcopy(arr)
            rotate()
    for i in range(n):
        print(' '.join(map(str, arr[i])))
