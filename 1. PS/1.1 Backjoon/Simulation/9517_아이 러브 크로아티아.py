import sys
sys.stdin = open('9517.txt')

K = int(input())
N = int(input())
# 210
total_time = 0
for i in range(N):
    T, Z = input().split()
    total_time += int(T)
    if total_time > 210:
        break
    if Z == 'T':
        K += 1
    if K > 8:
        K %= 8

print(K)