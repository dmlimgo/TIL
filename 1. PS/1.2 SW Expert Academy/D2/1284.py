T = int(input())
for tc in range(T):
    P, Q, R, S, W = map(int, input().split())
    A_fee = W * P
    if W <= R:
        B_fee = Q
    else:
        B_fee = Q + S * (W - R)
    if A_fee > B_fee:
        print(f'#{tc + 1} {B_fee}')
    else:
        print(f'#{tc + 1} {A_fee}')