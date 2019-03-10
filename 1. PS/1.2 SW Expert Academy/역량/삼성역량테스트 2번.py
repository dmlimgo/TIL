import sys
sys.stdin = open('samsung2.txt')

def drop(player, block):
    for x in range(100):
        if arr[block][x] == 0:
            arr[block][x] = player
            return 1
    return -1

def delete(player):
    flag = 0
    for x in range(99, -1, -1):
        status = []
        cnt = 1
        for y in range(6):
            if arr[y][x] == arr[y+1][x]:
                cnt += 1
            else:
                status.append((arr[y][x], cnt, y))
                cnt = 1
        for i in range(len(status)-1, -1, -1):
            if status[i][0] == 0:
                status.pop(i)
        for i in range(len(status)):
            if status[i][1] >= 4:
                flag = 1
                if status[i][0] == player:
                    score[player] += status[i][1]
                for j in range(status[i][1]):
                    arr[status[i][2]-j].pop(x)
                    arr[status[i][2]-j].append(0)
    if flag:
        return True
    else:
        return False




N = int(input())
block = list(map(int, input().split()))
arr = [[0 for _ in range(100)] for _ in range(7)]
score = [0, 0, 0]
for i in range(N):
    print(i)
    if i % 2 == 0:
        drop(1, block[i])
        print('player1 drop')
        for i in range(7):
            print(arr[i])
        while delete(1):
            print('player1 delete')
            for i in range(7):
                print(arr[i])
            print('p1 get score', score)
            continue

    else:
        drop(2, block[i])
        print('player2 drop')
        for i in range(7):
            print(arr[i])
        while delete(2):
            print('player2 delete')
            for i in range(7):
                print(arr[i])
            print('p2 get score', score)
            continue

