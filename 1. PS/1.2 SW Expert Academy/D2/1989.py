T = int(input())
for tc in range(T):
    pal = input()
    if pal == pal[::-1]:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')