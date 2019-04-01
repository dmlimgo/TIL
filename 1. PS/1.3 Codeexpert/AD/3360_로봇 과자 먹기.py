import sys
sys.stdin = open('3360.txt')

def perm(pos, dis):
    global minval
    if dis > minval:
        return
    if pos == N:
        if dis < minval:
            minval = dis
        return
    for i in range(pos, N):
        A[pos], A[i] = A[i], A[pos]
        perm(pos+1, dis + memo[pos][A[pos]])
        A[pos], A[i] = A[i], A[pos]

T = int(input())
for tc in range(T):
    N = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))

    R = []
    S = []
    for i in range(N):
        R.append((robot[i * 2], robot[i * 2 + 1]))
        S.append((snack[i * 2], snack[i * 2 + 1]))
    A = list(range(N))
    memo = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            memo[j][i] = abs(R[i][0]-S[j][0]) + abs(R[i][1]-S[j][1])
    minval = 10000001
    perm(0, 0)
    print('%d' % (minval))