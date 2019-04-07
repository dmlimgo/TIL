N, K, L = map(int, input().split())
round = 1
while True:
    if abs(K-L) == 1 and min(K,L) % 2:
        break
    K = (K+1)//2
    L = (L+1)//2
    round += 1
print(round)



'''
1 2 3 4 5 6 7 8 9 10 11
1   2   3   4   5    6
1       2       3
1               2
1
'''