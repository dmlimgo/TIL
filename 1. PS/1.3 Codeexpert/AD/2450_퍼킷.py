import sys
sys.stdin = open('2450.txt')

def part(pos, gob, hap, cnt):
    global minval
    if pos == N:
        cha = abs(gob - hap)
        if minval > cha:
            minval = cha
        return
    part(pos+1, gob * tastes[pos][0], hap + tastes[pos][1], 0)
    if cnt == N-1:
        return
    part(pos+1, gob, hap, cnt + 1)

N = int(input())
tastes = []
for i in range(N):
    s, b = map(int, input().split())
    tastes.append((s, b))
minval = 10000001
part(0, 1, 0, 0)
print(minval)