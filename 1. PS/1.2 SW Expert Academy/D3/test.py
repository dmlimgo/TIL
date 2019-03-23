import sys
sys.stdin = open('t1.txt')
a = []
for i in range(1000):
    a.append(input())
sys.stdin = open('t2.txt')
for i in range(1000):
    if a[i] != input():
        print(i,'wrong')
    else:
        print(i)