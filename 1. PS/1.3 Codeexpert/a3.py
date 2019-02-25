n = int(input())

mi = []
ma = []
for i in range(n):
    c, s = input().split()
    c = int(c)
    if s == 'Y':
        if not ma:
            ma.append(c)
        elif ma and ma[0] > c:
            ma[0] = c
    elif s == 'N':
        if not mi:
            mi.append(c)
        elif mi and mi[0] < c:
            mi[0] = c

if mi >= ma:
    print('F')
else:
    print(ma[0])