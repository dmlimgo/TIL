rode = [64]
X = int(input())
while sum(rode) > X:
    stick = rode.pop()
    rode.append(stick // 2)
    rode.append(stick // 2)
    if sum(rode[:-1]) >= X:
        rode.pop()
print(len(rode))