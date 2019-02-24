dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
arr = [[0 for _ in range(3)] for _ in range(3)]
moves = 0

def find_way(x1, y1, arr):
    global moves
    moves += 1
    for d in range(4):
        newX = x1 + dx[d]
        newY = y1 + dy[d]
        if newX < 0 or newY < 0 or newX > 2 or newY > 2 or arr[newY][newX]:
            continue
        print(arr)
        arr[newY][newX] = 1
        find_way(newY, newX, arr)
    return 0


while True:
    try:
        start, end = input().split()
        x1, y1 = 1, 1
        x2, y2 = 0, 0
        arr[y1][x1] = 1
        arr[y2][x2] = 0
        if x1 == x2 and y1 == y2:
            break
        find_way(x1, y1, arr)
    except ValueError:
        break
print(f'To get from {start} to {end} takes {moves} knight moves.')