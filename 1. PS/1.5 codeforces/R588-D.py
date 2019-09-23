n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tmp = {}
cand = []
for i in range(n):
    if A[i] in tmp:
        tmp[A[i]] += 1
    else:
        tmp[A[i]] = 1
for k, v in tmp.items():
    if v > 1:
        cand.append(bin(k)[2:][::-1])
cand_len = list(map(len, cand))
def shortenbin(c):
    return bin(c)[2:][::-1]
A = list(map(shortenbin, A))
A_len = list(map(len, A))
# print(cand)
# print(A)
if len(cand) == 0:
    print(0)
else:
    maxVal = 0
    for i in range(len(cand)):
        hap = 0
        for j in range(n):
            if cand_len[i] < A_len[j]: continue
            cand_better = True
            for k in range(A_len[j]):
                if cand[i][k] == '0' and A[j][k] == '1':
                    cand_better = False
                    break
            if cand_better:
                hap += B[j]
        if hap > maxVal:
            maxVal = hap
    print(maxVal)
    # 뛰어난 사람 여럿있으면 다 더해줘야함...