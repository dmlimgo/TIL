arr = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
sum = 0
for i in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(10):
        for j in range(10):
            if arr[y+i][x+j]:
                continue
            else:
                arr[y+i][x+j] = 1
                sum += 1
print(sum)
