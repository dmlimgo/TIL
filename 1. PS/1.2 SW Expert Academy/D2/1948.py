T = int(input())
ed = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    day = sum(ed[m1-1:m2-1]) - (d1 - 1) + d2
    print(f'#{tc+1} {day}')