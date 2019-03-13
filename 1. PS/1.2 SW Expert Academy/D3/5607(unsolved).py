
def combination(n, r):
    for i in range(2, n+1):
        comb.append(comb[-1] * i)

T = int(input())
for tc in range(T):
    N, R = map(int, input().split())
    comb = [1]
    combination(N, R)
    print(comb)