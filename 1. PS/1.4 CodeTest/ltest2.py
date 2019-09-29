import sys
sys.stdin = open('2.txt')

expr = list(input())
cha = []
num = []
for i in range(len(expr)):
    if expr[i].isnumeric():
        if expr[i] == '1' and i < len(expr)-1 and expr[i+1] == '0':
            num.append('10')
        elif expr[i] == '0':
            continue
        else:
            num.append(expr[i])
    else:
        if expr[i+1].islower():
            cha.append(expr[i]+expr[i+1])
        elif expr[i].islower():
            continue
        else:
            cha.append(expr[i])
if len(cha) != len(num):
    print('error')
else:
    for i in range(len(cha)):
        print(cha[i], end='')
        if num[i] != '1':
            print(num[i], end='')