T = int(input())
for tc in range(T):
    n = input()
    cnt = 0
    tmp = '0'
    for i in n:
        if i != tmp:
            tmp = i
            cnt += 1
    print(f'#{tc+1} {cnt}')
