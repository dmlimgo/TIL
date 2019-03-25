S, X = input().split()
X = int(X)
size = len(S)
for i in range(1, size):
    if int(S[:i]) + int(S[i:]) == X:
        print('{}+{}={}'.format(int(S[:i]), int(S[i:]), X))
        break
else:
    print('NONE')