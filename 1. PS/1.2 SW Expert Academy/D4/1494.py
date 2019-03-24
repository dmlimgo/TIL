import sys
sys.stdin = open('1494.txt')

# 인터넷 코드 분석 안함 아직
def dfs(pos):
    global N, num
    if num // 2:
        print(haveTeam)
        return
    for i in range(pos+1, N):
        if not haveTeam[i]:
            haveTeam[i] = True
            for j in range(N):
                if not haveTeam[j]:
                    haveTeam[j] = True
                    team[i] = team[j] = num
                    num += 1
                    dfs(i)
                    num -= 1
                    haveTeam[j] = False
            haveTeam[i] = False
            break


T = int(input())
for tc in range(2):
    N = int(input())
    worm = []
    for i in range(N):
        worm.append((list(map(int, input().split()))))
    ans = -1
    haveTeam = [0] * N
    team = [0] * N
    num = 0
    dfs(-1)