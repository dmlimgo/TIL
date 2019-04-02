import sys
sys.stdin = open('3363.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
perm()
