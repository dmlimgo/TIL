import sys
sys.stdin = open("2275.txt")
import time
start2 = time.time()
n, m = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0

while True:
    sum = 0
    mid = (start + end) // 2

    if mid == result :
        break

    for i in range(n):
        if data[i] > mid:
            sum += data[i] - mid

    if sum > m:
        start = mid + 1
        result = mid
    elif sum == m:
        result = mid
        break
    else:
        end = mid - 1
print(result)
print(time.time()-start2)