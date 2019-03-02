# 190302 13:15
import sys
sys.stdin = open('4008.txt')

def make_base(op):
    ops = '+-*/'
    result = ''
    for i in range(len(op)):
        result += ops[i]*op[i]
    return result

def make_cands(k, size):
    a = [0] * size

    for i in range(1, k):
        a

def make_permutation(base, k):
    size = len(base)
    if k == size:
        add_cands(k)
    else:
        k += 1
        ncands = make_cands(k, size)

    return cand_list

T = int(input())
for tc in range(1):
    N = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    base = make_base(op)
    cand_list = make_permutation(base, 0)