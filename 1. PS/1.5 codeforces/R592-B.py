t = int(input())
for tc in range(t):
    n = int(input())
    rooms = input()
    fx = -1
    lx = -1
    for i in range(len(rooms)):
        if rooms[i] == '1':
            if fx == -1:
                fx = i
            lx = i
    if lx == -1:
        print(n)
    else:
        print(max((n-fx)*2, (lx+1)*2))