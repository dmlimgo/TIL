import sys
sys.stdin = open('2624.txt')

import math
def findtwo():
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return x, y

N = int(input())
arr = [0] * N
for n in range(N):
    arr[n] = list(map(int, list(input())))
xt, yt = findtwo()

max = 0
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            d = math.ceil(((xt-x)**2 + (yt-y)**2)**0.5)
            if max < d:
                max = d
print(max)