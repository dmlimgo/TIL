import sys
sys.stdin = open('3362.txt')

def dfs(pos):
    global done, final_node
    if pos == N:
        final_node = nodes
        done = 1
        return
    color = []
    for i in range(N):
        if arr[pos][i]:
            color.append(nodes[i])
    for i in range(1, M + 1):
        if i not in color:
            nodes[pos] = i
            dfs(pos+1)
            if done:
                return

N, M = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split())) + [0] * (N-i-1)
for j in range(N):
    for i in range(N):
        arr[j][i] = arr[i][j]

nodes = [0] * N
final_node = [0] * N
done = 0
dfs(0)
if set(final_node) == set(range(1, M+1)):
    print(' '.join(map(str, final_node)))
else:
    print(-1)
