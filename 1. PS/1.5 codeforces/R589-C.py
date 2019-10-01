def prime(x):
    tmp = []
    i = 2
    n = x
    while i * i <= x:
        while n % i == 0:
            tmp.append(i)
            n /= i
            i += 1
        i += 1
    return tmp
def g(x, p):
    i = 0
    ans = 1
    while True:
        pi = (p**i)
        if pi * pi > x:
            break
        else:
            if x % pi == 0:
                ans = pi
        i += 1
    return ans
def f(x, n):
    x_arr = prime(x)
    ans = 1
    for x in x_arr:
        ans *= g(n, x)
    return ans
        
x, n = map(int, input().split())
res = 1
for i in range(1, n+1):
    res = (res * f(x, i))%1000000007
print(res)