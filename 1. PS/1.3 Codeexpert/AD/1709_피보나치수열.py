def pibo(n):
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]
arr = [1, 1]
print(pibo(int(input())-1))