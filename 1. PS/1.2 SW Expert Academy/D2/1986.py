T = int(input())
for tc in range(T):
    N = int(input())
    hap = 0
    for i in range(1, N+1):
        if i % 2:
            hap += i
        else:
            hap -= i
    print(f'#{tc+1} {hap}')