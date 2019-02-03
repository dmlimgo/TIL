import sys
sys.stdin = open("D2_2007_input.txt")

T = int(input())
for tc in range(T):
    sen = input()
    for level in range(1, 11):
        if sen[:level] == sen[level:2*level] and sen[:level] == sen[2*level:3*level]:
            print(f'#{tc+1} {level}')
            break