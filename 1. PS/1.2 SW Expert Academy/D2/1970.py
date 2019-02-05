T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(T):
    n = int(input())
    print(f'#{tc + 1}')
    for i in range(8):
        print(n // money[i], end = ' ')
        n %= money[i]
    print()

