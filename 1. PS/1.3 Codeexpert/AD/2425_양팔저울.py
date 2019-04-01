import sys
sys.stdin = open('2425.txt')

def part(pos, left, right):
    if pos == N:
        cha = abs(sum(left)-sum(right))
        possible.append(cha)
        return
    part(pos+1, left, right)
    part(pos+1, left+[WN[pos]], right)
    part(pos+1, left, right+[WN[pos]])


N = int(input())
WN = list(map(int, input().split()))
M = int(input())
WM = list(map(int, input().split()))

maxW = sum(WN)
possible = []
part(0, [], [])
possible = list(set(possible))
# print(possible)
for i in range(M):
    if WM[i] in possible:
        print('Y', end=' ')
    else:
        print('N', end=' ')