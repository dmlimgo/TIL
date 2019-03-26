import sys
sys.stdin = open('2731.txt')
import time
start = time.time()
def dfs(pos, hap):
    global N, minval
    if pos == N:
        print(hap)
        return
    minimum = min(arr[pos])
    dfs(pos+1, hap + minimum)

def dfs2(pos, hap):
    global N, minval
    if hap >= minval:
        return
    if pos == N:
        # if hap < minval:
        minval = hap
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs2(pos+1, hap + arr[pos][i])
            visit[i] = 0

def dfs3(pos, hap, tmp):
    global N, minval
    # print(visit, pos, hap)
    if pos == N:
        print(tmp)
        if hap < minval:
            minval = hap
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs3(pos + 1, hap + arr[pos][i], tmp +[arr[pos][i]])
            visit[i] = 0

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
dfs(0, 0)
# visit = [0] * N
# minval = 1000001
# dfs3(0, 0, [])
# print(minval)
visit = [0] * N
minval = 1000001
dfs2(0, 0)
print(minval)
print(time.time()-start)