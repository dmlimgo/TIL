import time

start = time.time()
a = []
for i in range(300000):
    a.append(i)
print(time.time()-start)

start = time.time()
b = len(set(a))
print(b)
print(time.time()-start)

start = time.time()
b = 0
for i in range(len(a)):
    if a:
        b += 1
print(b)
print(time.time()-start)