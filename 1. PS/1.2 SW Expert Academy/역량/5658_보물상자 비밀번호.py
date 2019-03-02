# 190302 12:03
import sys
sys.stdin = open('input.txt')

def convert(num, base):
    L = "0123456789ABCDEF"
    i, j = divmod(num, base)

    if i == 0:
        return L[j]
    else:
        return convert(i, base) + L[j]

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    nums = input()
    result = []
    for i in range(N//4):
        result.append(int(nums[0:N//4], 16))
        result.append(int(nums[N//4:N//4*2], 16))
        result.append(int(nums[N//4*2:N//4*3], 16))
        result.append(int(nums[N//4*3:N], 16))
        nums = nums[-1] + nums[:-1]
    print(f'#{tc+1} {sorted(list(set(result)), reverse=True)[K-1]}')