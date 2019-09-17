def check(m):
    
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    W = list(map(int, input().split()))
    S = list(map(int, input().split()))
    s, e = 1, 200000
    while s < e:
        m = (s+e)//2
        check(m)