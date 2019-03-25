N = int(input())
sum = 0
narr = [0] * 1001
start = 1001
end = 0

max = 0
for n in range(N):
    x, y = map(int, input().split())
    narr[x] = y
    if x > end:
        end = x
    if x < start:
        start = x
    if y > max:
        max = y
        lmax_index = max_index = x

sum += narr[max_index]

while True:
    lmax = 0
    if lmax_index == start:
        break
    for l in range(lmax_index-1, start-1, -1):
        if narr[l] > lmax:
            lmax = narr[l]
            lindex = l
    sum += lmax * (lmax_index - lindex)
    lmax_index = lindex

while True:
    rmax = 0
    if max_index == end:
        break
    for r in range(max_index+1, end+1):
        if narr[r] > rmax:
            rmax = narr[r]
            rindex = r
    sum += rmax * (rindex - max_index)
    max_index = rindex

print(sum)


# while True:
#     lmax = 0
#     for l in range(max_index-1, 0, -1):
#         if narr[l] > lmax:
#             lmax = narr[l]
#             lindex = l
#     sum += lmax * (end - max_index)
#     max_index = lindex
#     if max_index == start:
#         break




# h = 0
# i = 0
# while i != end+1:
#     for x in range(i+1, end+1):
#         if narr[x]:
#
#             if narr[x] > narr[i]:
#                 next_h = narr[x]
#                 for e in range(i, x):
#                     sum += h
#                 i = x
#                 h = next_h
#
#
#     sum += h
#     if i == end:
#         break