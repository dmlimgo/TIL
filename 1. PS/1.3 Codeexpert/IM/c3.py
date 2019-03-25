def divide(x, y):
    global cnt
    sum_a = sum_b = sum_c = sum_d = 0
    for b in range(y+1):
        sum_a += sum(arr[b][:x+1])
        sum_b += sum(arr[b][x+1:])
    for b in range(y+1, N):
        sum_c += sum(arr[b][:x+1])
        sum_d += sum(arr[b][x+1:])
    if sum_a == sum_b and sum_b == sum_c and sum_c == sum_d:
        cnt += 1

N = int(input())
arr = [0 for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, list(input())))
cnt = -1
for y in range(N):
    for x in range(N):
        divide(x, y)
if cnt > -1:
    print(cnt + 1)
else:
    print(cnt)