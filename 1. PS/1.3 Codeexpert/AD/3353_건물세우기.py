import sys
sys.stdin = open('3353.txt')

def dfs(pos, sum):
    global n, minval
    if sum >= minval:
        return
    if pos == n:
        minval = sum
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            dfs(pos+1, sum+arr[pos][i])
            visit[i] = 0


n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
visit = [0] * n
minval = 1000001
dfs(0, 0)
print(minval)