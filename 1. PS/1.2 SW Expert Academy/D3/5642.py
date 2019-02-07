T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    mx = arr[0]
    hap = 0
    for i in range(N):
        hap = hap + arr[i]
        if hap < 1:
            hap = 0
        if hap > mx:
            mx = hap
    print(f'#{tc+1} {mx}')