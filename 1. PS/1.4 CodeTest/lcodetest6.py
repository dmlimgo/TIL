N, M = input().split()
N = int(N)
nH = 0
order = []
size = []
for i in range(N):
    w, nums = input().split()
    w = int(w)
    a = list(map(int, list(nums)))
    order += a
    for j in a:
        size += [w]
    if w > nH:
        nH = w
nH = nH*2-1
numArr = [''] * 10
numArr[0] = ['.' * size[0] + '#'] * nH
for i in range(nH):
    numArr[0][i]

    