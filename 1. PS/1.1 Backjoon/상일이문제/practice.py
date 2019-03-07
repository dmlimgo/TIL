import time
now = time.time()
a = [0,1,2]
for i in range(1000):
    narr = [[0 for _ in range(300)] for _ in range(300)]
print(time.time()-now)
