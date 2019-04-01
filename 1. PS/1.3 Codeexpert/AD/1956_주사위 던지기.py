import sys
sys.stdin = open('1956.txt')

def Rperm(pos):
    if pos == N:
        print(' '.join(map(str, A)))
        return
    for i in range(1, 7):
        A[pos] = i
        Rperm(pos+1)
        A[pos] = 0

def Rcomb(pos):
    if pos == N:
        print(' '.join(map(str, A)))
        return
    for i in range(1, 7):
        if pos > 0 and A[pos-1] > i:
            continue
        A[pos] = i
        Rcomb(pos+1)
        A[pos] = 0

def perm(pos):
    if pos == N:
        print(' '.join(map(str, A)))
        return
    for i in range(1, 7):
        if not visit[i]:
            visit[i] = 1
            A[pos] = i
            perm(pos + 1)
            A[pos] = 0
            visit[i] = 0

N, M = map(int, input().split())
A = [0] * N
if M == 1:
    Rperm(0)
elif M == 2:
    Rcomb(0)
else:
    visit = [0] * 7
    perm(0)