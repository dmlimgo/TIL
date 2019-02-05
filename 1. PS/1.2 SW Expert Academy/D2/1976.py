T = int(input())
for tc in range(T):
    h1,m1,h2,m2 = map(int, input().split())
    m1 = divmod(m1 + m2, 60)
    h1 = divmod(h1 + h2 + m1[0], 12)
    if h1[1] == 0:
        print(f'#{tc+1} 12 {m1[1]}')
    else:
        print(f'#{tc + 1} {h1[1]} {m1[1]}')
