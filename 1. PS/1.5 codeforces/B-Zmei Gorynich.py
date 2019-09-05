T = int(input())
for tc in range(T):
    n, x = map(int, input().split())
    max_deal = 0
    max_d = 0
    for t in range(n):
        d, h = map(int, input().split())
        if max_deal < d-h: max_deal = d-h
        if max_d < d: max_d = d
    if max_d >= x:
        print(1)
        continue
    else:
        if max_deal <= 0:
            print(-1)
            continue
    if (x - max_d) % max_deal == 0:
        print((x - max_d)//max_deal + 1)
    else:
        print((x - max_d)//max_deal + 2)
    
