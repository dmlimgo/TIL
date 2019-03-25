import sys
sys.stdin = open('1860.txt')

def solve(order, time, fish):
    j = len(order)-1
    while j >= 0:
        if time != 0 and time % M == 0:
            fish += K
        while j >= 0 and order[j] == time:
            if fish == 0:
                return 0
            j -= 1
            fish -= 1
        time += 1
    return 1

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    order = sorted(list(map(int, input().split())), reverse=True)

    if solve(order, 0, 0):
        print('#%d Possible' % (tc+1))
    else:
        print('#%d Impossible' % (tc + 1))

# def solve(order, time, fish):
#     while order:
#         if time != 0 and time % M == 0:
#             fish += K
#         while order and order[-1] == time:
#             if fish == 0:
#                 return 0
#             order.pop()
#             fish -= 1
#         time += 1
#     return 1
#
# T = int(input())
# for tc in range(T):
#     N, M, K = map(int, input().split())
#     order = sorted(list(map(int, input().split())), reverse=True)
#
#     if solve(order, 0, 0):
#         print('#%d Possible' % (tc+1))
#     else:
#         print('#%d Impossible' % (tc + 1))