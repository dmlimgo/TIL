n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tmp = {}
cand = []
def shortenbin(c):
    return bin(c)[2:][::-1]
for i in range(n):
    if A[i] in tmp:
        tmp[A[i]] += 1
    else:
        tmp[A[i]] = 1
for k, v in tmp.items():
    if v > 1:
        cand.append(shortenbin(k))
cand_len = list(map(len, cand))
A = list(map(shortenbin, A))
A_len = list(map(len, A))
skill_set = [0] * 60
for c in cand:
    for i in range(len(c)):
        if c[i]:
            skill_set[i] = 1
visit = [0] * n
if len(cand) == 0:
    print(0)
else:
    # print(cand, A, skill_set)
    
    for i in range(n):
        better = 1
        for j in range(A_len[i]):
            if A[i][j] == '1' and skill_set[j] == 0:
                better = 0
                break
        if better:
            visit[i] = 1
    hap = 0
    for i in range(n):
        if visit[i]:
            hap += B[i]
    print(hap)