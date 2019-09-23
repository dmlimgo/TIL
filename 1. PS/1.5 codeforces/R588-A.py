candy = list(map(int, input().split()))
hap = sum(candy)
pos = False
for i in range(4):
    if candy[i] == hap/2:
        pos = True
for i in range(3):
    for j in range(i+1, 4):
        if candy[i] + candy[j] == hap/2:
            pos = True
for i in range(2):
    for j in range(i+1, 3):
        for k in range(j+1, 4):
            if candy[i] + candy[j] + candy[k] == hap/2:
                pos = True
if pos:
    print('YES')
else:
    print("NO")