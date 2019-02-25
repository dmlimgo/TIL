def find(nu):
    global max, max_origin
    original = int(nu)
    while len(nu) > 1:
        a = 0
        for k in nu:
            a += int(k)
        nu = str(a)
    if int(nu) > max:
        max_origin = original
        max = int(nu)
    elif int(nu) == max:
        if max_origin > original:
            max_origin = original
            max = int(nu)

n = int(input())
max = 0
max_origin = 0
for i in range(n):
    nu = input().strip()
    find(nu)
print(max_origin)