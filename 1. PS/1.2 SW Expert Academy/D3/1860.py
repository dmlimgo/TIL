import sys
sys.stdin = open('1860.txt')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    order = list(map(int, list(input())))
    for i in range(N):
