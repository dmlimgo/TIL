import sys
sys.stdin = open('2688.txt')

def find(anyarr, n):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == n:
                anyarr.append((x, y))

def c_dis(c_arr):
    hap = 0
    for each in house:
        mindis = 1000001
        for chick in c_arr:
            dis = abs(each[0] - chick[0]) + abs(each[1] - chick[1])
            if mindis > dis:
                mindis = dis
        hap += mindis
    return hap

def part(pos, c_arr):
    global minval
    if len(c_arr) > M:
        return
    if pos == L:
        dis = c_dis(c_arr)
        # print(dis, c_arr)
        if dis < minval and dis != 0:
            minval = dis
        return

    part(pos+1, c_arr + [chicken[pos]])
    part(pos+1, c_arr)


N, M  = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
find(chicken, 2)
find(house, 1)
L = len(chicken)
# print('chicken:', chicken)
# print('house:  ', house)
minval = 1000001
part(0, [])
print(minval)