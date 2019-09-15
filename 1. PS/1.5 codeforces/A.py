n = int(input())
arr = list(map(int, input().split()))
narr = []
# sarr = []
for i in range(n):
    tmp = []
    for j in range(2, arr[i]+1):
        if arr[i] % j == 0:
            tmp.append(j)
            # if j not in sarr:
                # sarr.append(j)
    narr.append(tmp)
print(narr)
# sarr.sort()
# print(sarr)
# for i in range(len(sarr)-1):
#     if sarr[i] == 0: continue
#     for j in range(i+1, len(sarr)):
#         if sarr[j] == 0: continue
#         if sarr[j] % sarr[i] == 0:
#             sarr[j] = 0
# cnt = 0
# print(sarr)
# for i in range(len(sarr)):
#     if sarr[i]: cnt += 1
# print(cnt)

