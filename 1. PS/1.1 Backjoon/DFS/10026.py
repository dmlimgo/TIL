import sys
sys.stdin = open('10026.txt')
import copy
sys.setrecursionlimit(10000000)

def find(arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'R': return x, y, 'R'
            if arr[y][x] == 'G': return x, y, 'G'
            if arr[y][x] == 'B': return x, y, 'B'
    return -1, -1, -1

def area(x, y, alphabet, arr):
    global cnt, N
    arr[y][x] = ' '
    for d in range(4):
        newX = x + dx[d]
        newY = y + dy[d]
        if newX < 0 or newY < 0 or newX > N-1 or newY > N-1 or arr[newY][newX] != alphabet:
            continue
        area(newX, newY, alphabet, arr)

def change():
    for y in range(N):
        for x in range(N):
            if carr[y][x] == 'G':
                carr[y][x] = 'R'

N = int(input())
arr = [[0] for _ in range(N)]
carr = [[0] for _ in range(N)]
for i in range(N):
    arr[i] = list(input())
carr = copy.deepcopy(arr)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 0
while True:
    x, y, alphabet = find(arr)
    if x == -1:
        break
    area(x, y, alphabet, arr)
    cnt += 1
print(cnt, end=' ')

change()
cnt = 0
while True:
    x, y, alphabet = find(carr)
    if x == -1:
        break
    area(x, y, alphabet, carr)
    cnt += 1
print(cnt)