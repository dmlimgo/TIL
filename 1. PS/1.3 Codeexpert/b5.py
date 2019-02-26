import copy

def match(x, y):
    global N
    for j in range(N):
        for i in range(N):
            if arr[y + j][x + i] != pat[j][i]:
                return 0
    return 1

def rotate():
    global N
    for y in range(N):
        for x in range(N):
            pat[y][x] = npat[N-x-1][y]

M = int(input())
arr = [[0 for _ in range(M)] for _ in range(M)]
for m in range(M):
    arr[m] = list(map(int, list(input())))
N = int(input())
pat = [[0 for _ in range(N)] for _ in range(N)]
for n in range(N):
    pat[n] = list(map(int, list(input())))
npat = copy.deepcopy(pat)


tsum = 0
for i in range(4):
    # for k in range(N):
    #     print(pat[k])
    for y in range(M-N+1):
        for x in range(M-N+1):
            tsum += match(x, y)
    rotate()
    npat = copy.deepcopy(pat)
print(tsum)
