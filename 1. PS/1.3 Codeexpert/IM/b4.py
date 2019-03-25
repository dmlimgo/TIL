def match(x, y):
    for j in range(N):
        for i in range(N):
            if arr[y + j][x + i] != pat[j][i]:
                return 0
    return 1

M = int(input())
arr = [[0 for _ in range(M)] for _ in range(M)]
for m in range(M):
    arr[m] = list(map(int, list(input())))
N = int(input())
pat = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
    pat[n] = list(map(int, list(input())))

sum = 0
for y in range(M-N+1):
    for x in range(M-N+1):
        sum += match(x, y)

print(sum)
