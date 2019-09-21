# Q = int(input())
# for q in range(Q):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     while True:
#         tmp = {}
#         for i in range(len(arr)):
#             if arr[i] > 2048:
#                 continue
#             if arr[i] in tmp:
#                 tmp[arr[i]] = 1
#             else:
#                 tmp[arr[i]]
Q = int(input())
for q in range(Q):
    N = int(input())
    arr = list(map(int, input().split()))
    hap = 0
    for i in range(len(arr)):
        if arr[i] > 2048: continue
        hap += arr[i]
    if hap >= 2048:
        print('YES')
    else:
        print('No')
