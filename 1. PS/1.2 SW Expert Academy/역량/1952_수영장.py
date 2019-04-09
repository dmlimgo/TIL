import sys
sys.stdin = open('1952.txt')

def dfs(pos, hap):
    global minval
    if hap > minval:
        return
    if pos > 12:
        if hap < minval:
            minval = hap
        return
    dfs(pos+1, hap + PLAN[pos-1] * F1)
    dfs(pos+1, hap + F2)
    dfs(pos+3, hap + F3)

T = int(input())
for tc in range(T):
    F1, F2, F3, F4 = map(int, input().split())
    PLAN = list(map(int, input().split()))
    minval = F4
    dfs(1, 0)
    print('#%d %d' % (tc+1, minval))