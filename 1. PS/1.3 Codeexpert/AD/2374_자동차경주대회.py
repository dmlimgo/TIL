import sys
sys.stdin = open('2374.txt')

def part(pos, dis, time, last):
    global minval
    if dis > MaxD:
        return
    if time > minval:
        return
    if pos == N+1:
        if last == N+1:
            if time < minval:
                minval = time
            return
        return

    part(pos+1, memo[last][pos+1], time+NT[pos+1], pos+1)
    part(pos+1, memo[last][pos+1], time, last)


MaxD = int(input())
N = int(input())
ND = list(map(int, input().split()))
NT = [0] + list(map(int, input().split())) + [0]

memo = [[0 for _ in range(N+2)] for _ in range(N+2)]
for j in range(N+1):
    for i in range(j+1, N+2):
        hap = 0
        for d in range(j, i):
            hap += ND[d]
        memo[j][i] = hap
# for i in range(N+2):
#     print(memo[i])

minval = 10000001
part(0, 0, 0, 0)
print(minval)