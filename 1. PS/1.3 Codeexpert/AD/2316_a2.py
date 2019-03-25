N = int(input())
arr = list(map(int, input().split()))
T = int(input())
nums = list(map(int, input().split()))
for i in range(T):
    s, e = 0, N-1
    done = 0
    while s <= e:
        m = (s + e) // 2
        if arr[m] == nums[i]:
            print(m+1)
            done = 1
            break
        elif arr[m] > nums[i]:
            e = m - 1
        else:
            s = m + 1
    if not done:
        print(0)