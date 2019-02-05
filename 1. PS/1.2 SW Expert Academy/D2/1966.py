T = int(input())
for tc in range(T):
    N = input()
    arr = list(map(int, input().split()))
    print(f"#{tc + 1} {' '.join(map(str, sorted(arr)))}")