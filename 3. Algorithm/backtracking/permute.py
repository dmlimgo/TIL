def make_cands(a, k, size, c):
    perm = [0] * size
    for i in range(1, k):
        perm[a[i]] = 1

    ncands = 0
    for i in range(1, size):
        if perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, size):
    global cnt
    c = [0] * (size - 1)
    if k == size - 1:
        result.append(a[1:])
        cnt += 1
    else:
        k += 1
        ncands = make_cands(a, k, size, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, size)

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = len(data)
a = [0] * size
result = []
cnt = 0
backtrack(a, 0, size)
print('cnt:', cnt)