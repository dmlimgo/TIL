import sys
sys.stdin = open('3280.txt')

def part(pos, A, B):
    global maxval
    if len(B) > 1 and B[-2] >= B[-1]:
        return
    if len(A) > 1 and A[-2] <= A[-1]:
        return
    if pos == N:
        hap = sum(A[1:]) + sum(B[1:])
        if hap > maxval:
            maxval = hap
        return
    part(pos + 1, A, B + [Size[pos]])
    part(pos + 1, A + [Size[pos]], B)
    part(pos + 1, A, B)


T = int(input())
for tc in range(T):
    N = int(input())
    Size = list(map(int, input().split()))

    visit = [0] * N
    maxval = 0
    part(0, [10001], [0])
    print(maxval)




    # for i in range(N):
    #     visit = [0] * N
    #     A = [10001]
    #     visit[i] = 1
    #     B = [Size[i]]
    #     for j in range(i, N):
    #         if B[-1] < Size[j] and not visit[j]:
    #             visit[j] = 1
    #             B.append(Size[j])
    #     for j in range(i, N):
    #         if A[-1] > Size[j] and not visit[j]:
    #             visit[j] = 1
    #             A.append(Size[j])
    #     hap = sum(A[1:]) + sum(B)
    #     if hap > maxval:
    #         print(A[1:], B)
    #         maxval = hap
    # print(maxval)
