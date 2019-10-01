n, k = map(int, input().split())
arr = list(map(int, input().split()))
msg = {}
s = e = 0
for q in arr:
    try:
        if s <= msg[q] <= e:
            pass
        else:

    except KeyError:
        s -= 1
        msg[q] = s
        if e - s > k:
            e -= 1
        
        

for i in range(??):
    print(msg[i], end=" ")