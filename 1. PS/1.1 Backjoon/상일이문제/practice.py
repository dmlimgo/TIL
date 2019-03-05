import sys
import copy

sys.stdin = open('p.txt')
def solve(res, new_exp):
    global maxval
    for i in res:
        a = int(new_exp.pop(i-1))
        op = new_exp.pop(i-1)
        b = int(new_exp.pop(i-1))
        if op == '+': new_exp.insert(i-1, a+b)
        if op == '-': new_exp.insert(i-1, a-b)
        if op == '*': new_exp.insert(i-1, a*b)
    result = int(new_exp[0])
    for i in range(1, len(new_exp), 2):
        if new_exp[i] == '+': result += int(new_exp[i+1])
        if new_exp[i] == '-': result -= int(new_exp[i+1])
        if new_exp[i] == '*': result *= int(new_exp[i+1])
    if maxval < result:
        maxval = result


def permutation(res):
    global N
    new_exp = copy.deepcopy(exp)
    solve(res[::-1], new_exp)
    for i in range(3, N, 2):
        if not visit[i] and num[i] > res[-1] + 3:
            visit[i] = 1
            permutation(res + [num[i]])
            visit[i] = 0


N = int(input())
exp = list(input())
if N == 1:
    print(exp[0])
else:
    N -= 1
    num = list(range(N))
    visit = [0] * N
    maxval = -1000001
    new_exp = copy.deepcopy(exp)
    solve([1], new_exp)
    for i in range(3, N, 2):
        visit[i] = 1
        permutation([i])
        visit[i] = 0
    print(maxval)

