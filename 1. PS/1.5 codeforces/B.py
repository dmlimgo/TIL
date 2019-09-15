n = int(input())
led = list(map(int, list(input())))
L = len(led)
order = []
for i in range(n):
    order.append(list(map(int, input().split())))
if L == sum(led):
    print(L)
else:
    max_val = 0
    for t in range(100000):
        hap = 0
        for j in range(L):
            if t < order[j][1]:
                hap += led[j]
            else:
                tmp = (t-order[j][1]-1) % (order[j][0]*2)
                if tmp < order[j][0]:
                    hap += not led[j]
                else:
                    hap += led[j]
        if hap > max_val:
            max_val = hap
    print(max_val)
    