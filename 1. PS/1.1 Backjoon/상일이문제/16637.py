import sys
import copy

sys.stdin = open('p.txt')
def solve(res, new_exp):
    global maxval
    for i in res:
        # print(res, i, new_exp)
        a = int(new_exp.pop(i-1))
        # print(res, i, a, new_exp)
        op = new_exp.pop(i-1)
        # print(res, i, op, new_exp)
        b = int(new_exp.pop(i-1))
        # print(res, i, b, new_exp)
        if op == '+': new_exp.insert(i-1, a+b)
        if op == '-': new_exp.insert(i-1, a-b)
        if op == '*': new_exp.insert(i-1, a*b)
        # print(res, i, new_exp)
    result = int(new_exp[0])
    for i in range(1, len(new_exp), 2):
        if new_exp[i] == '+': result += int(new_exp[i+1])
        if new_exp[i] == '-': result -= int(new_exp[i+1])
        if new_exp[i] == '*': result *= int(new_exp[i+1])
    # print(result)
    if maxval < result:
        maxval = result


def permutation(res):
    global N
    # print(res[::-1])
    new_exp = copy.deepcopy(exp)
    solve(res[::-1], new_exp)
    for i in range(3, N, 2):
        if not visit[i] and num[i] > res[-1] + 3:
            visit[i] = 1
            permutation(res + [num[i]])
            visit[i] = 0


N = int(input())
exp = list(input())
N -= 1
num = list(range(N))
visit = [0] * N
maxval = -1000001
# print(N, num)
new_exp = copy.deepcopy(exp)
solve([1], new_exp)
for i in range(3, N, 2):
    visit[i] = 1
    permutation([i])
    visit[i] = 0
print(maxval)



# def solve(k, res):
#     print(k, res)
#     if k == N-1:
#         print(res)
#         return
#     if susik[k] == '+': solve(k+1, int(res) + int(susik[k+1]))
#     if susik[k] == '-': solve(k+1, int(res) - int(susik[k+1]))
#     if susik[k] == '*': solve(k+1, int(res) * int(susik[k+1]))
#     if susik[k].isnumeric() : solve(k+1, res)
#
#
# N = int(input())
# susik = list(input())
# solve(0, susik[0])



