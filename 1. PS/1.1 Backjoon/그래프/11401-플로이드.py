import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = [[100001 for _ in range(N)] for _ in range(N)]
for i in range(M):
    s, e, p = map(int, input().split())
    arr[s][e] = min(arr[s][e], p)

