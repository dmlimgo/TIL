N = int(input())
acron = list(map(int, input().split()))

smart = 0
smart_cnt = 0
idot_max = -1000000001
idot = 0
minus_cnt = 0
# min = 10001
max = -10001
for i in acron:
    if max < i:
        max = i
    if i >= 0:
        smart_cnt += 1
        smart += i
    idot += i
    if idot < 0:
        minus_cnt += 1
        idot = 0
    if idot > idot_max:
        idot_max = idot
    # print(idot, idot_max)
if minus_cnt == len(acron):
    idot_max = max
if smart_cnt == 0:
    smart = max
print(idot_max, smart)