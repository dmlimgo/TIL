import sys
sys.stdin = open('2681.txt')

def comb(pos, last, arr):
    if pos == M:
        arr.sort()
        if arr not in pod:
            pod.append(arr)
        return
    for i in range(last+1, N):
        comb(pos+1, i, arr + [Nlist[i]])


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    Nlist = list(map(int, input().split()))
    pod = []
    comb(0, -1, [])
    print(len(pod))