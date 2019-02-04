T = int(input())
for tc in range(T):
    N = int(input())
    print(f'#{tc+1}')
    a = [0,1]
    cnt = 0
    while cnt < N:
        b = a[:]
        for i in range(1, len(a)):
            print(a[i] + a[i-1], end = ' ')
            b[i] = a[i] + a[i-1]
        b.append(0)
        a = b
        print()
        cnt += 1

