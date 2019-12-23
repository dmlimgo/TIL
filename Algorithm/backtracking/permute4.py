def solve(pos, res):
    global N
    # if pos == N:
    #     print(res)
    print(pos, res)
    for i in range(1, N, 2):
        if not visit[i] and num[i] > res[-1] + 3:
            visit[i] = 1
            solve(pos + 1, res+[num[i]])
            visit[i] = 0

N = 10
num = list(range(N))
visit = [0] * N
print(N, num)
for i in range(1, N, 2):
    visit[i] = 1
    solve(0, [i])
    visit[i] = 0



# def solve(pos, n1, n2, n3, n4, res):
#     if pos == N:
#         print(res)
#     if n1 != 1: solve(pos + 1, n1 + 1, n2, n3, n4, res + [num[0]])
#     if n2 != 1: solve(pos + 1, n1, n2 + 1, n3, n4, res + [num[1]])
#     if n3 != 1: solve(pos + 1, n1, n2, n3 + 1, n4, res + [num[2]])
#     if n4 != 1: solve(pos + 1, n1, n2, n3, n4 + 1, res + [num[3]])
#
#
# N = 4
# num = [1, 2, 3, 4]
# solve(0, 0, 0, 0, 0, [])


# def solve(pos, n1, n2, n3, n4, res):
#     if pos == N:
#         print(res)
#     if n1 != 1: solve(pos + 1, n1 + 1, n2, n3, n4, res + num[0] + ' ')
#     if n2 != 1: solve(pos + 1, n1, n2 + 1, n3, n4, res + num[1] + ' ')
#     if n3 != 1: solve(pos + 1, n1, n2, n3 + 1, n4, res + num[2] + ' ')
#     if n4 != 1: solve(pos + 1, n1, n2, n3, n4 + 1, res + num[3] + ' ')
#
#
# N = 4
# num = ['1', '2', '3', '4']
# res = ''
# solve(0, 0, 0, 0, 0, res)