s = input()
Q = int(input())
for q in range(Q):
    a, b, c = input().split()
    if a == '1':
        b = int(b)
        s = s[:b-1] + c + s[b:]
    else:
        l = int(b)
        r = int(c)
        cnt = 0
        tmp = {}
        for i in range(l-1, r):
            try:
                if tmp[s[i]]:
                    pass
            except KeyError:
                tmp[s[i]] = 1
                cnt += 1
        print(cnt)