K = int(input())
N = int(input())
total = 0
done = 0
for n in range(N):
    t, z = input().split()
    t = int(t)
    if z == 'T':
        total += t
        if total > 210:
            print(K)
            done = 1
            break
        K += 1
        if K > 8:
            K %= 8
    elif z == 'P' or z =='F':
        total += t
        if total > 210:
            print(K)
            done = 1
            break
if not done:
    print(K)