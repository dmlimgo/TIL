a, b = map(int, input().split())
n = 0
val = 1
while True:
    val *= 1.5
    n += 1
    if val > b/a:
        break
print(n)