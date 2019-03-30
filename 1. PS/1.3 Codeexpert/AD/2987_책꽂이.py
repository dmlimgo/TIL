import sys
sys.stdin = open('2987.txt')

def comb(pos, hap):
    global minval
    if hap > minval:
        return
    if pos == N:
        if minval > hap >= B:
            minval = hap
        return
    comb(pos+1, hap+cows[pos])
    comb(pos+1, hap)

T = int(input())
for tc in range(T):
    N, B = map(int, input().split())
    cows = []
    for i in range(N):
        cows.append(int(input()))
    minval = 1000001
    comb(0, 0)
    print(minval-B)