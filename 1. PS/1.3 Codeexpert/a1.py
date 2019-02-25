p = input()
sum = 10
for i in range(1, len(p)):
    if p[i] == p[i-1]:
        sum += 5
    else:
        sum += 10
print(sum)