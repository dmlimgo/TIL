T = int(input())
for tc in range(T):
    N = int(input())
    sett = set()
    i = 1
    while True:
        sett = sett | set(str(N*i))
        if len(sett) == 10:
            break
        i += 1
    print(f'#{tc+1} {i*N}')