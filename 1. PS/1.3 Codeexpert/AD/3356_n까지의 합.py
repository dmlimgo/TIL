def rec(n):
    if n < 2: return 1
    return n + rec(n-1)
print(rec(int(input())))