T = int(input())
for tc in range(T):
    d = input()
    data = list(map(int, input().split()))
    set_data = set(data)
    max_cnt = 0
    max_data = 0
    for i in set_data:
        if data.count(i) > max_cnt:
            max_cnt = data.count(i)
            max_data = i
        elif data.count(i) == max_cnt:
            if i > max_data:
                max_data = i
    print(f'#{tc+1} {max_data}')