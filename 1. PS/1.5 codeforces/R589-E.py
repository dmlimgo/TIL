import math
n, k = map(int, input().split())
n_fac = math.factorial(n)
ans = n_fac*(9**(n**2-n)) - (n_fac-1)
#경우의 수 따지기...