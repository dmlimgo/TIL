def permutation(k):
    global size, cnt
    if k == size:
        tmp = []
        for i in range(size):
            tmp.append(output[i])
        result.append(tmp)
        cnt += 1
    else:
        for i in range(size):
            if not visit[i]:
                visit[i] = 1
                output[k] = data[i]
                permutation(k+1)
                visit[i] = 0


data = [2,2,3]
size = len(data)
output = [0] * size
visit = [0] * size
result = []
cnt = 0
permutation(0)
print(result)
print(cnt)
