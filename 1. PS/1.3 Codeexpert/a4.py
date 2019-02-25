y, x = map(int, input().split())
arr = [[0 for _ in range(x)] for _ in range(y)]
for i in range(y):
    arr[i] = list(map(int, input().split()))


for j in range(y):
    cnt = 0
    for i in range(x):
        if arr[j][i] == 0:
            cnt = 0
        else:
            cnt += 1
        print(cnt, end=" ")
    print()