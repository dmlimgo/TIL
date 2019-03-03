# 190303 13:51
import sys
sys.stdin = open('4008.txt')

def op_permu(k):
    # DFS로 순열 생성
    global N
    # if k == N-1:
    #     tmp2 = []
    #     for p in range(N-1):
    #         tmp2.append(output[p])
    #     # if tmp2 not in result:
    #     #     result.append(tmp2)
    #     result.append(tmp2)
    if k == N - 1:
        tmp2 = [0] * (N-1)
        for p in range(N - 1):
            tmp2[p] = output[p]
        result.append(tmp2)
    else:
        cands = make_cands(k)
        for j in range(4):
            if cands[j]:
                output[k] = data[j]
                op_permu(k+1)

def optonum(data):
    if data == '+':
        return 0
    elif data == '-':
        return 1
    elif data == '*':
        return 2
    elif data == '/':
        return 3

def make_cands(until):
    cands = [0,0,0,0]
    for i in range(4):
        cands[i] = op_cnt[i]
    for i in range(until):
        if output[i] == '+':
            cands[0] -= 1
        elif output[i] =='-':
            cands[1] -= 1
        elif output[i] =='*':
            cands[2] -= 1
        elif output[i] =='/':
            cands[3] -= 1
    return cands

def operate(z):
    a = exp.pop(0)
    b = exp.pop(0)
    if result[each][z - 1] == '+':
        c = a + b
    elif result[each][z - 1] == '-':
        c = a - b
    elif result[each][z - 1] == '*':
        c = a * b
    elif result[each][z - 1] == '/':
        c = int(a / b)
    exp.append(c)

T = int(input())
for tc in range(T):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    data = ['+','-','*','/']
    output = [0] * (N-1)
    result = []

    op_permu(0)
    # print(result)
    for each in range(len(result)):
        exp = []
        exp.append(numbers[0])
        for z in range(1, len(numbers)):
            exp.append(numbers[z])
            operate(z)
        if each == 0:
            # 첫번째 결과로 max, min 초기화
            maxn = minn = exp[0]
        if maxn < exp[0]:
            maxn = exp[0]
        if minn > exp[0]:
            minn = exp[0]
    print(f'#{tc+1} {maxn-minn}')



# def convert():
#     # 연산자 숫자 받아서 문자열로 나열
#     ops = '+-*/'
#     data = ''
#     for i in range(4):
#         data += ops[i] * op_cnt[i]
#     return list(data)