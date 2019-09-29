l, r = map(int, input().split())
ans = -1
for i in range(l, r+1):
    nums = [0] * 10
    ok = 1
    for d in str(i):
        d = int(d)
        if nums[d]: 
            ok = 0
            break
        else: 
            nums[d] = 1
    if ok:
        ans = i
        break
print(ans)
    




