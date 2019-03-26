import sys
f = open('practice.txt', 'w')
for i in range(1, 1000001):
    data = str(i) + ' '
    f.write(data)
f.close()