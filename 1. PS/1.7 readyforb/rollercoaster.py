import sys
sys.stdin = open('1.txt')
import time
start = time.time()

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0]+list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        arr[i][0] = ((arr[i][1]-1)/arr[i][2])      
    arr.sort(reverse=True)
    sol = 1
    for i in range(N):
        sol = (sol*arr[i][1] + arr[i][2])%1000000007
    print(f'#{tc+1} {sol}')