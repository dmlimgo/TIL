T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] * N
    for n in range(N):
        arr[n] = int(input())
    avg = int(sum(arr) / len(arr))
    move = 0
    for n in range(N):
        move += abs(arr[n] - avg)
    print(f'#{tc+1} {int(move/2)}')