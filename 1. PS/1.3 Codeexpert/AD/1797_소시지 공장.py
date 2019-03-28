import sys
sys.stdin = open('1797.txt')

def solve(i):
    for j in range(len(works)):
        if i[0] >= works[j][0] and i[1] >= works[j][1]:
            works[j] = i
            return True
    return False

N = int(input())
arr = list(map(int, input().split()))
meat = []
for i in range(len(arr)//2):
    meat.append((arr[i*2],arr[i*2+1]))
meat.sort()
works = [meat.pop(0)]
for i in meat:
    if not solve(i):
        works.append(i)
print(len(works))
