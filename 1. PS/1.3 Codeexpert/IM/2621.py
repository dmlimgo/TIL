N, S = input().split()
N = int(N)
degree = 0

i = 0
while i < len(S):
    # print(S[i], degree)
    if S[i] == '<':
        degree += 1
        if degree == N:
            k = 1
            while S[i+k].isnumeric():
                print(S[i+k], end='')
                k += 1
            if k > 1:
                print(end= ' ')
            i += k-1
    elif S[i] == '>':
        degree -= 1
    i += 1

#---
# for i in range(len(S)):
#     print(S[i],degree)
#     if S[i] == '<':
#         degree += 1
#         if degree == N:
#             print(S[i+1], end='')
#     elif S[i] == '>':
#         degree -= 1