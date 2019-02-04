import sys
sys.stdin = open("D2_2001_input.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    max_fly = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            fly = 0
            for z in range(M):
                fly = fly + sum(arr[y+z][x:x+M])
            if fly > max_fly:
                max_fly = fly
    print(f'#{tc+1} {max_fly}')

