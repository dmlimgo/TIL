n, p, w, d = map(int, input().split())
x = -1
# print('wd/d', (w-d)//d)
mz = 0
imp = 0
for z in range((w-d)//d):
    # print(z, (p + (z-n)*d) % (w-d), (p + (z-n)*d) // (w-d))
    if (p + (z-n)*d) % (w-d) == 0:
        mz = z
        break
# print('mz', mz)
for i in range(1, 1000000000000):
    tmp = (p + (mz-n)*d + (w-d)*i) // (w-d)
    if tmp >= 0:
        x = tmp
        rz = mz + (w-d)*i//d
        if rz > n:
            imp = 1
            break
        if n-x-rz >= 0:
            break
if x == -1 or imp:
    print(-1)
else:
    print(x, n-x-rz, rz)