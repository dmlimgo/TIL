frog = {'c':0, 'r':1, 'o':2, 'a':3, 'k':4}
T = int(input())
for tc in range(T):
    test = input()
    result = []
    stat = 1
    if test[0] != 'c':
        print(f'#{tc+1} -1')
        continue
    else:
        result.append(0)
    for i in test[1:]:
        for r in range(len(result)):            # 모든 result에 대해서 돌린다.
            a = 0
            if (result[r]+1) % 5 == frog[i]:    # r=0 의 다음 문자이면
                result[r] += 1                  # r=0 의 울음을 한칸 옮긴다
                a = 1
                break
        else:                                   # r=0 의 다음 문자가 아니면
            if i == 'c' and a == 0:             # r=1 의 첫문자인지 확인
                result.append(0)                # r을 추가
            else:
                result = [3]
                break
    for r in result:
        if (r % 5) != 4:
            print(f'#{tc + 1} -1')
            break
    else:
        print(f'#{tc+1} {len(result)}')