import collections
n, k = map(int, input().split())
ani = collections.deque([])
for i in range(k):
    ani.append(list(map(int, input().split())))
s_check = [0 for _ in range(n+1)]
s_check[0] = 1
sat = 0
while ani:
    x, y = ani.popleft()
    
    if s_check[x] == 0 or s_check[y] == 0:
        sat += 1
        s_check[x], s_check[y] = 1, 1
    if sat == k:
        break
    L = len(ani)
    i = -1
    while True:
        i += 1
        # print(ani, i)
        if i >= L:
            break
        if s_check[ani[i][0]] and s_check[ani[i][1]]: 
            del ani[i]
            L -= 1
            i -= 1
            continue
        if ani[i][0] == x or ani[i][1] == x or ani[i][0] == y or ani[i][1] == y:
            if s_check[ani[i][0]] == 0 or s_check[ani[i][1]] == 0:
                sat += 1
                s_check[ani[i][0]], s_check[ani[i][1]] = 1, 1
                del ani[i]
                L -= 1
        
# print(s_check)
print(k-sat)

    
