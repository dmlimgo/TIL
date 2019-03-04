N = int(input())
acron = list(map(int, input().split()))

smart = 0
smart_cnt = 0
idot_max = -1000000001
min = 10001
max = -10001
for i in range(len(acron)):
    if min > acron[i]:
        min = acron[i]
    if max < acron[i]:
        max = acron[i]
    if acron[i] >= 0:
        smart_cnt += 1
        smart += acron[i]
    idot = 0
    for j in range(i, len(acron)):
        idot += acron[j]
        if idot > idot_max:
            idot_max = idot
    # if idot < 0:
    #     idot = i
    # if idot > idot_max:
    #     idot_max = idot
if smart_cnt == 0:
    smart = max
print(idot_max, smart)