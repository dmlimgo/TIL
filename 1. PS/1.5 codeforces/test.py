import time
start = time.time()
A = [1 for i in range(10000000)]
for i in range(len(A)):
    if A[i]:
        A[i] = 1
print(time.time()-start)

start = time.time()
A = [1 for i in range(5000000)] + [0 for i in range(5000000)]
for i in range(len(A)):
    if A[i]:
        A[i] = 1
print(time.time()-start)

start = time.time()
A = [0 for i in range(10000000)]
for i in range(len(A)):
    if A[i]:
        A[i] = 1
print(time.time()-start)

start = time.time()
A = [1 for i in range(10000000)]
for i in range(len(A)):
    A[i] = 1
print(time.time()-start)

start = time.time()
A = [1 for i in range(5000000)] + [0 for i in range(5000000)]
for i in range(len(A)):
    A[i] = 1
print(time.time()-start)

start = time.time()
A = [0 for i in range(10000000)]
for i in range(len(A)):
    A[i] = 1
print(time.time()-start)