def bs(s, e, d):
    m = sol = -1
    while s <= e:
        m = (s + e)//2
        if case[m] < d:
            s = sol = m + 1
        else:
            e = m - 1
        # print(s, m, e, d, sol)
    return sol

N = int(input())
case = [0]
for n in range(N):
    case.append(int(input()))
case.sort()
cnt = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        jump = case[j] - case[i]
        cnt += bs(1, N, case[j] + 2*jump+1) - bs(1,N, case[j]+jump)
        # print(cnt)
print(cnt)