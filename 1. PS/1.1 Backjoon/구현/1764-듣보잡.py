N, M = map(int, input().split())
names = []
for i in range(N+M):
    names.append(input())
heards = set(names[:N])
saws = set(names[N:])
res = list(heards & saws)
res.sort()
print(len(res))
for r in res:
    print(r)