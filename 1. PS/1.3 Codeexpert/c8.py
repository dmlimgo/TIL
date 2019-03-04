a, b = map(int, input().split())
if a > b:
    a, b = b, a
num = [2]
for i in range(3, b+1):
    cnt = 0
    for j in num:
        if j > i ** (1 / 2):
            break
        if i % j == 0:
            cnt = 1
            break
    if cnt == 0:
        num.append(i)
for i in range(len(num)):
    if num[i] >= a:
        sosu_min = num[i]
        min_index = i
        break
for i in range(len(num)-1, -1, -1):
    if num[i] <= b:
        sosu_max = num[i]
        max_index = i
        break
print(max_index-min_index+1)
print(sosu_min+sosu_max)


# for i in range(a, b+1):
#     cnt = 0
#     for n in num:
#         if i % num == 0:
#             cnt += 1
#     if cnt == 2:
#         num
#         sosu_cnt += 1
#         if sosu_min > i:
#             sosu_min = i
#         if sosu_max < i:
#             sosu_max = i
# print(sosu_cnt, sosu_max, sosu_min)