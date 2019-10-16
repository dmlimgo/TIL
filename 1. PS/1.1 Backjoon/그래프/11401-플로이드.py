def dfs(s, n):
    print('sn', s,n)
    for e in range(1, N+1):
        if bus[n][e] != 0:
            res[s][e] = min(res[s][e], res[s][n] + bus[n][e])
            dfs(s, e)
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
bus = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    s, e, p = map(int, input().split())
    bus[s][e] = p
res = [[100001 for _ in range(N+1)] for _ in range(N+1)]
for s in range(1, N+1):
    dfs(s, s)
for i in range(N+1):
    print(res[i])
    