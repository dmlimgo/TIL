T = int(input())
for tc in range(T):
    s, t, e = map(int, input().split())
    sol = int((t-s+e)//2)
    if e == 0:
        if s > t: print(1)
        else: print(0)
    else:
        if sol < 0: print(e+1)
        elif sol > e: print(0)
        else: print(e-sol)
    