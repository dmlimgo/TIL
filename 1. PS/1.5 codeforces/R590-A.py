Q = int(input())
for q in range(Q):
    n = int(input())
    arr = list(map(int, input().split()))
    hap = sum(arr)
    print((hap+n-1)//n)