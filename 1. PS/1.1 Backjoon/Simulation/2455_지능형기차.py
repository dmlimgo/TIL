sum = 0
maxval = 0
for i in range(4):
    off, on = map(int, input().split())
    sum += on-off
    if sum > maxval:
        maxval = sum
print(maxval)