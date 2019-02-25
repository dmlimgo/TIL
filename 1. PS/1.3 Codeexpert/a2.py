T = int(input())
A = 300
B = 60
C = 10
a = b = c = 0
while T >= 10:
    a = T // A
    T %= A
    b = T // B
    T %= B
    c = T // C
    T %= C
if T:
    print(-1)
else:
    print(a, b, c)
