import sys
sys.stdin = open('2545.txt')

N = int(input())
tapes = list(map(int, input().split()))
A = []
B = []
tapes.sort(reverse=True)
while tapes:
    if sum(A) <= sum(B):
        if len(A) == N//2:
            B.append(tapes.pop(0))
        else:
            A.append(tapes.pop(0))
    else:
        if len(B) == N//2:
            A.append(tapes.pop(0))
        else:
            B.append(tapes.pop(0))
# print(A, B)
# print(sum(A), sum(B))
dif = abs(sum(A) - sum(B))
minval = dif
if sum(A) > sum(B):
    for i in range(N//2):
        for j in range(N//2):
            if 0 < (A[i] - B[j]) < dif:
                newdif = abs(sum(A) - sum(B) - 2*(A[i] - B[j]))
                if newdif < dif:
                    dif = newdif
elif sum(A) < sum(B):
    for i in range(N//2):
        for j in range(N//2):
            if 0 < (B[i] - A[j]) < dif:
                newdif = abs(sum(B) - sum(A) - 2*(B[i] - A[j]))
                if newdif < dif:
                    dif = newdif
print(dif)