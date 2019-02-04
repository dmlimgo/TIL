import sys
sys.stdin = open("1859_input.txt")

T = int(input())
for tc in range(T):
    d = input()
    price = list(map(int, input().split()))

    max_index = 0
    max_change = 1
    amount = 0
    spend = 0
    profit = 0
    for i in range(len(price)):
        if max_change:
            max_price = max(price[max_index:])
            max_change = 0
        if price[i] != max_price:
            spend += price[i]
            amount += 1
        else:
            profit += price[i] * amount - spend
            amount = spend = 0
            max_index = i + 1
            max_change = 1
    print(f'#{tc+1} {profit}')