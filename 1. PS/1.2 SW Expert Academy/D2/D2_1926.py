N = int(input())
for i in range(1, N+1):
    new_i = str(i)
    cnt = 0
    for x in new_i:
        if int(x) % 3 == 0 and int(x) != 0:
            cnt += 1
    if cnt:
        print('-' * cnt, end = ' ')
    else:
        print(i, end = ' ')

