#190302 01:30
import sys
sys.stdin = open("5644.txt")

def checkAP(x, y):
    global A
    check = []
    for i in range(A):
        if abs(x - ap[i][0]) + abs(y - ap[i][1]) <= ap[i][2]:
            check.append(i)
    return check

def Samearea():
    for i in range(len(checkA)):
        for j in range(len(checkB)):
            if checkA[i] == checkB[j]:
                return True
    return False

def Connect():
    max_charge = 0
    for i in checkA:
        for j in checkB:
            if i == j:
                charge_sum = ap[i][3]
            else:
                charge_sum = ap[i][3] + ap[j][3]
            if max_charge < charge_sum:
                max_charge = charge_sum
    return max_charge

# def Connect():
#     if len(checkA) == 1 and len(checkB) == 1:
#         b_charge = ap[checkA[0]][3]
#         return b_charge
#     if len(checkA) < len(checkB):
#         shorter = checkA
#         longer = checkB
#     else:
#         shorter = checkB
#         longer = checkA
#     s_charge = 0
#     l_charge = 0
#     for i in shorter:
#         if s_charge < ap[i][3]:
#             s_charge = ap[i][3]
#             used = i
#     for i in longer:
#         if i == used:
#             continue
#         if l_charge < ap[i][3]:
#             l_charge = ap[i][3]
#     return l_charge + s_charge

def charge(check):
    b_charge = 0
    for i in check:
        if b_charge < ap[i][3]:
            b_charge = ap[i][3]
    return b_charge

area = [[0 for _ in range(11)] for _ in range(11)]
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

T = int(input())
for tc in range(T):
    M, A = map(int, input().split())
    ma = list(map(int, input().split()))
    mb = list(map(int, input().split()))
    ap = []
    for i in range(A):
        ap.append(list(map(int, input().split())))
    ax = ay = 1
    bx = by = 10
    total = 0
    for i in range(M+1):
        checkA = checkAP(ax, ay)
        checkB = checkAP(bx, by)
        if Samearea():
            total += Connect()
        else:
            total += charge(checkA)
            total += charge(checkB)
        # 마지막거 끊어주기
        if i == M:
            # print(i, total)
            break
        # 이동
        ax += dx[ma[i]]
        ay += dy[ma[i]]
        bx += dx[mb[i]]
        by += dy[mb[i]]
        # print(i, total)
    print(f'#{tc+1} {total}')
