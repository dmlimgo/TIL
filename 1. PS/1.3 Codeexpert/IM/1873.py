N = int(input())
arr = [0 for _ in range(N)]
for n in range(N):
    arr[n] = list(map(int, input().split()))
new_arr = [[0 for _ in range(N)] for _ in range(3)]
for i in range(3):
    for j in range(N):
        new_arr[i][j] = arr[j][i]
print(new_arr)
result = [[],[],[]]
for i in range(3):
    result[i].append(new_arr[i].count(3))
    result[i].append(new_arr[i].count(2))
    result[i].append(new_arr[i].count(1))
print(result)
result.sort(reverse=True)
print(result)


