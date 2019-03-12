def dfs(d):
    global visit, k
    if d == 6:
        for i in range(6):
            print(result[i], end=' ')
        print()
    else:
        for i in range(k):
            if not visit[i] and result[d-1] < S[i]:
                visit[i] = 1
                result[d] = S[i]
                dfs(d+1)
                visit[i] = 0


while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    k = nums[0]
    S = nums[1:]
    visit = [0] * k
    result = [0] * 7
    dfs(0)
    print()