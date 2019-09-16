import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append([0] + list(map(int, input().split())))
        arr[i][0] = ((arr[i][1]-1)/arr[i][2])      
    arr.sort(reverse=True)
    # print(arr)
    # sol = 1
    # for i in range(N):
    #     sol = sol*arr[i][1] + arr[i][2]
    # print(f'#{tc+1} {sol%1000000007}')
    arr[0][0] = 1 * arr[0][1] + arr[0][2]
    # print(arr)
    # print('---')
    for i in range(1, N):
        # print('i')
        arr[i][0] = arr[i-1][0]*arr[i][1] + arr[i][2]
    # print(arr)
    print(f'#{tc+1} {arr[-1][0]%1000000007}')