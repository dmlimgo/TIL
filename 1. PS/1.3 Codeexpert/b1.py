def define():
    global x1, x2, y1, y2, xd1, xd2, yd1, yd2
    for y in range(100):
        for x in range(100):
            if arr[y][x] == 3:
                return 3
    sum1 = sum2 = 0
    for y in range(y1 - 1, y1 + yd1 + 1):
        sum1 += arr[y][x1 - 1]
        sum2 += arr[y][x1 + xd1]
    if sum(arr[y1-1][x1-1:x1+xd1+1]) == 0 and sum(arr[y1+yd1][x1-1:x1+xd1+1]) == 0:
        if sum1 == 0 and sum2 == 0:
            return 4
    # print(sum(arr[y1-1][x1-1:x1+xd1+1]))
    # print(sum(arr[y1+yd1][x1-1:x1+xd1+1]))
    # print(sum1)
    # print(sum2)
    bordersum = sum(arr[y1-1][x1-1:x1+xd1+1]) + sum(arr[y1+yd1][x1-1:x1+xd1+1]) + sum1 + sum2
    if bordersum == 4:
        return 1
    if bordersum > 4:
        return 2


x1, y1, xd1, yd1 = map(int, input().split())
x2, y2, xd2, yd2 = map(int, input().split())
arr = [[0 for _ in range(100)] for _ in range(100)]

for y in range(y1, y1+yd1):
    for x in range(x1, x1+xd1):
        arr[y][x] += 1
for y in range(y2, y2+yd2):
    for x in range(x2, x2+xd2):
        arr[y][x] += 2
# for i in range(100):
#     print(arr[i])
print(define())
