import sys
sys.stdin = open('samsung2.txt')

def drop(player, block):



N = int(input())
block = list(map(int, input().split()))
arr = [[0 for _ in range(100)] for _ in range(6)]
for i in range(N):
    if i % 2 == 0:
        drop(1, block[i])
    else:
        drop(2, block[i])
