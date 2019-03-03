# 190304 12:03
import sys
sys.stdin = open('4013.txt')

def check(num):
    checked = [0] * 5
    checked[num] = 1
    for i in range(num, 1, -1):
        if mg[i][6] != mg[i-1][2] and checked[i]: checked[i-1] = 1
        else: checked[i-1] = 0
    for i in range(num, 4):
        if mg[i][2] != mg[i+1][6] and checked[i]: checked[i+1] = 1
        else: checked[i+1] = 0
    return checked

def rotate(num, d):
    if d == 1:
        mg[num] = [mg[num][-1]] + mg[num][:-1]
    else:
        mg[num] = mg[num][1:] + [mg[num][0]]

def define(num, d):
    for r in rot:
        if r[num] == d:
            return r

rot = [[0, 1, -1, 1, -1], [0, -1, 1, -1, 1]]
T = int(input())
for tc in range(T):
    K = int(input())
    mg = [0]
    for i in range(4):
        mg.append(list(map(int, input().split())))
    # S = 0, N = 1
    # 시계 = 1, 반시계 -1
    for k in range(K):
        num, d = map(int, input().split())
        checked = check(num)
        r = define(num, d)
        for i in range(1, 5):
            if checked[i]:
                rotate(i, r[i])
    score = 0
    for i in range(1, 5):
        if mg[i][0] == 1:
            score += 2**(i-1)
    print(f'#{tc+1} {score}')
