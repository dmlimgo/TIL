import sys
sys.stdin = open("1983_input.txt")

rank = 'A+ A0 A- B+ B0 B- C+ C0 C- D0'.split()
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [0 for _ in range(N)]
    for n in range(N):
        e1, e2, e3 = map(int, input().split())
        arr[n] = e1*0.35 + e2*0.45 + e3*0.2
    harry = arr[K-1]
    rank_arr = sorted(arr, reverse = True)
    print(f'#{tc+1} {rank[int(rank_arr.index(harry)/(N/10))]}')

    # 10명이면 0  ,1  ,2  ,3  ,4  ,5    ,6    ,7  ,8  ,9
    # 20명이면 0~1,2~3,4~5,6~7,8~9,10~11,12~13
    # 30명이면 0~2,3~5,6~8,9~