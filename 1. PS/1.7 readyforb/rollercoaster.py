import sys
sys.stdin = open('1.txt')
import time
start = time.time()

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0]+list(map(int, input().split())) for _ in range(N)]
    #---
    # arr = [0] * N
    # narr = list(map(lambda n: [0]+list(map(int, input().split())), arr))
    #---
    # arr = []
    for i in range(N):
    #     arr.append([0] + list(map(int, input().split())))
        arr[i][0] = ((arr[i][1]-1)/arr[i][2])      
    # print(narr)
    print(time.time() - start)
    arr.sort(reverse=True)
    print(time.time() - start)
    #---------
    sol = 1
    for i in range(N):
        sol = sol*arr[i][1] + arr[i][2]
    print(f'#{tc+1} {sol%1000000007}')
    print(time.time() - start)
    #---------
    # arr[0][0] = 1 * arr[0][1] + arr[0][2]
    # print(arr)
    # print('---')
    # for i in range(1, N):
        # print('i')
        # arr[i][0] = arr[i-1][0]*arr[i][1] + arr[i][2]
    # print(arr)
    # print(f'#{tc+1} {narr[-1][0]%1000000007}')