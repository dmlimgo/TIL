T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    m = min(map(abs, arr))
    cnt = arr.count(m) + arr.count(-m)
    print(f'#{tc+1} {cnt}')
# C로 다시 풀어야함..
