import sys
sys.stdin = open('16926.txt')

N, M, R = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotate():
    for n in range(N):
        for m in range(M):
            if 0 <= m < min(N,M)//2 and m <= n < N-m-1:
                narr[n+1][m] = arr[n][m]
            elif N-n-1 <= m < M-N+n and N-min(N,M)//2 <= n < N:
                narr[n][m+1] = arr[n][m]
            elif M-min(N,M)//2 <= m < M and M-m <= n < N-M+m+1:
                narr[n-1][m] = arr[n][m]
            elif n+1 <= m < M-n and 0 <= n < min(N,M)//2:
                narr[n][m-1] = arr[n][m]

# for i in range(N):
#     print(arr[i])
for i in range(R):
    narr = [[0 for _ in range(M)] for _ in range(N)]
    rotate()
    arr = narr
# print()
for i in range(N):
    print(' '.join(map(str, arr[i])))