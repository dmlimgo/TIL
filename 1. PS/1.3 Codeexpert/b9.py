import decimal

N = int(input())
arr = [0 for _ in range(N)]
for n in range(N):
    arr[n] = float(input())
max = 0
gob = 1
for i in range(N):
    if 1 > gob:
        gob = arr[i]
    elif 1 <= gob:
        gob = gob * arr[i]
    if gob > max:
        max = gob

D = decimal.Decimal
max = D(str(max))
print(max.quantize(D('0.001'), rounding=decimal.ROUND_HALF_UP))

# for i in range(N):
#     gob *= arr[i]
#     if max < gob:
#         max = gob
#     elif max < arr[i]:
#         max = arr[i]
#     if gob < 1:
#         gob = arr[i]