time_sum = 0
bonus = 0
for day in range(5):
    s, e = map(float, input().split())
    if (e-s) > 1 and (e-s) <= 5:
        bonus += (e-s-1) * 10000
        time_sum += (e - s - 1)
    elif (e-s) > 5:
        bonus += 40000
        time_sum += 4
if time_sum >= 15:
    bonus *= 0.95
elif time_sum <= 5:
    bonus *= 1.05
print(int(bonus))


