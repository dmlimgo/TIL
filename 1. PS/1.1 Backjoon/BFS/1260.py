import sys
sys.stdin = open('1260.txt')

def dfs(v):
    global N
    visit[v] = 1
    print(v, end=' ')
    for w in range(N+1):
        if arr[v][w] and not visit[w]:
            dfs(w)

def bfs(v):
    global N
    s.append(v)
    visit[v] = 1
    while s:
        x = s.pop(0)
        print(x, end=' ')
        for w in range(N+1):
            if arr[x][w] and not visit[w]:
                s.append(w)
                visit[w] = 1

N, M, V = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1
visit = [0] * (N+1)
dfs(V)
print()
s = []
visit = [0] * (N+1)
bfs(V)