import time

start_time = time.time()
a = list(range(100000))
a2 = map(lambda n: n*2, a)
end_time = time.time()
a3 = a2
print(a3)
fin = end_time - start_time
print(fin)