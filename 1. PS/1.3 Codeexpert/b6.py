N = int(input())
pick = list(map(int, input().split()))
arr = list(range(1, N+1))
for i in range(len(pick)):
    arr.insert(i - pick[i], arr[i])
    del arr[i+1]
print(' '.join(map(str, arr)))