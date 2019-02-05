T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    print(f'#{tc+1} {round(sum(arr)/len(arr))}')