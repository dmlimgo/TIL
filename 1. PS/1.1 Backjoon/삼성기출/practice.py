l = list(input())
for i in range(len(l)):
    if ord(l[i]) == 1:
        l[i] = ' '
print(''.join(map(str,l)))
