T = int(input())
for tc in range(T):
    N = int(input())
    print(f'#{tc+1}')
    cnt = 0
    for n in range(N):
        c, k = input().split()
        k = int(k)
        for i in range(k):
            cnt += 1
            print(c, end = '')
            if cnt == 10:
                print()
                cnt = 0
    print()