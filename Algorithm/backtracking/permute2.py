def permutation(index, k):
    global size, cnt
    output[k] = data[index]
    if k == size-1:
        fin = []
        for i in range(size):
             fin.append(output[i])
        result.append(fin)
        cnt += 1
        return
    for j in range(size):
        if visit[j] == 0:
            visit[j] = 1
            permutation(j, k+1)
            visit[j] = 0

data = [1, 2, 3, 4]
size = len(data)
output = [0] * size
visit = [0] * size
result = [] # 결과를 담을 리스트 선언
cnt = 0
for i in range(size):
    visit[i] = 1
    permutation(i, 0)
    visit[i] = 0
print('cnt:', cnt)