import sys
sys.stdin = open('2864.txt')

def part(pos, M, earned):
    global maxval
    if M == 0 or pos == C:
        earned += arr[M][pos]
        if earned > maxval:
            maxval = earned
        return

    for i in range(M+1):
        part(pos + 1, M - arr[i][0], earned + arr[i][pos])

M, C = map(int, input().split())
arr = [[0 for _ in range(C+1)]] + [list(map(int, input().split())) for _ in range(M)]
# for i in range(M+1):
#     print(arr[i])
maxval = -1000001
part(1, M, 0)
print(maxval)