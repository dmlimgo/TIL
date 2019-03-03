import sys
sys.stdin = open('4008.txt')

def solve(pos, sum, sub, mul, div, cur):
    global minVal, maxVal
    if pos == (N-1):
        if minVal > cur:
            minVal = cur
        if maxVal < cur:
            maxVal = cur
        return
    if(sum < op[0]): solve(pos + 1, sum + 1, sub, mul, div, cur + num[pos + 1])
    if(sub < op[1]): solve(pos + 1, sum, sub + 1, mul, div, cur - num[pos + 1])
    if(mul < op[2]): solve(pos + 1, sum, sub, mul + 1, div, cur * num[pos + 1])
    if(div < op[3] and num[pos + 1]): solve(pos + 1, sum, sub, mul, div + 1, int(cur / num[pos + 1]))


T = int(input())
for tc in range(T):
    minVal = 1000000009
    maxVal = -1000000009
    N = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))
    solve(0, 0, 0, 0, 0, num[0])
    print(f'#{tc+1} {maxVal-minVal}')
