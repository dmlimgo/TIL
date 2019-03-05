



def solve(k, res):
    print(k, res)
    if k == N-1:
        print(res)
        return
    if susik[k] == '+': solve(k+1, int(res) + int(susik[k+1]))
    if susik[k] == '-': solve(k+1, int(res) - int(susik[k+1]))
    if susik[k] == '*': solve(k+1, int(res) * int(susik[k+1]))
    if susik[k].isnumeric() : solve(k+1, res)


N = int(input())
susik = list(input())
solve(0, susik[0])



