import sys
sys.stdin = open('1966.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    prior = list(map(int, input().split()))
    index = list(range(N))
    prior = list(zip(prior, index))
    target = prior[M][1]
    cnt = 0
    while True:
        front = prior[0][0]
        exist = 0
        for i in range(1, len(prior)):
            if prior[i][0] > front:
                exist = 1
                break
        if exist:
            prior.append(prior.pop(0))
        else:
            cnt += 1
            prints = prior.pop(0)
            if target == prints[1]:
                print(cnt)
                break