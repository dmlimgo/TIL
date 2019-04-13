import sys
sys.stdin = open('1063.txt')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dir = {'L':0, 'LB':1, 'B':2, 'RB':3,
       'R':4, 'RT':5, 'T':6, 'LT':7}
arr = [[0 for _ in range(9)] for _ in range(9)]
K, S, N = input().split()
K, S, N = list(K), list(S), int(N)
K[0], K[1] = ord(K[0])-64, int(K[1])
S[0], S[1] = ord(S[0])-64, int(S[1])
for i in range(N):
    d = dir[input()]
    newX = K[0] + dx[d]
    newY = K[1] + dy[d]
    if newX < 1 or newY < 1 or newX > 8 or newY > 8:
        continue
    newSX = newSY = 0
    moved = 0
    if newX == S[0] and newY == S[1]:
        newSX = S[0] + dx[d]
        newSY = S[1] + dy[d]
        moved = 1
    if moved and (newSX < 1 or newSY < 1 or newSX > 8 or newSY > 8):
        continue
    K[0], K[1] = newX, newY
    if newSX and newSY:
        S[0], S[1] = newSX, newSY
print('%s%d' % (chr(K[0]+64), K[1]))
print('%s%d' % (chr(S[0]+64), S[1]))
# print(i)