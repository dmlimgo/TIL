import sys
sys.stdin = open('1905.txt')

def dfs(pos, hap, last):
    global N, K, result
    if sum(arr) < K:
        return
    if hap > K:
        return
    if hap == K:
        result = 1
        return
    if result:
        return
    for i in range(last, N):
        if not visit[i]:
            visit[i] = 1
            dfs(pos+1, hap+arr[i], i)
            visit[i] = 0

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # arr.sort(reverse=True)
    result = 0
    visit = [0] * N
    dfs(0, 0, 0)
    if result:
        print("YES")
    else:
        print("NO")