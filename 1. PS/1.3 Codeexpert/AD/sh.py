def perm(n,k):
    if n==k:
        print(A)
        global result
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(A[i] - A[j]) == (j - i):
                    return
        result += 1
    else:
        for i in range(k,n):
            A[i], A[k] = A[k], A[i]
            perm(n,k+1)
            A[i],A[k] = A[k],A[i]

n = int(input())
A = [i for i in range(n)]
result = 0
perm(n,0)
print(result)