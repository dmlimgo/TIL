dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
arr = [[0 for _ in range(8)] for _ in range(8)]
moves = 0

def find_way(x1, y1):
    global moves, arr
    moves += 1
    for d in range(8):
        newX = x1 + dx[d]
        newY = y1 + dy[d]
        if newX < 0 or newY < 0 or newX > 7 or newY > 7 or arr[newY][newX]:
            continue
        if arr[newY][newX] == 2:
            return ??


while True:
    try:
        start, end = input().split()
        x1, y1 = ord(start[0])-97, int(start[1])-1
        x2, y2 = ord(end[0])-97, int(end[1])-1
        arr[y1][x1] = 1
        arr[y2][x2] = 2
        if x1 == x2 and y1 == y2:
            break
        find_way(x1, y1)
    except ValueError:
        break
print(f'To get from {start} to {end} takes {moves} knight moves.')