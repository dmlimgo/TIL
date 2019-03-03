import sys
sys.stdin = open('4008.txt')

def calculate(k, hap, cha, gob, nan, res):
    global minVal, maxVal
    if k == N-1:
        if minVal > res:
            minVal = res
        if maxVal < res:
            maxVal = res
        return
    if hap < op[0]: calculate(k + 1, hap + 1, cha, gob, nan, res + num[k + 1])
    if cha < op[1]: calculate(k + 1, hap, cha + 1, gob, nan, res - num[k + 1])
    if gob < op[2]: calculate(k + 1, hap, cha, gob + 1, nan, res * num[k + 1])
    if nan < op[3]: calculate(k + 1, hap, cha, gob, nan + 1, int(res / num[k + 1]))


T = int(input())
for tc in range(T):
    N = int(input())
    op = list(map(int, input().split()))
    num = list(map(int, input().split()))
    minVal = 10000009
    maxVal = -10000009
    calculate(0, 0, 0, 0, 0, num[0])
    print(f'#{tc+1} {maxVal - minVal}')
