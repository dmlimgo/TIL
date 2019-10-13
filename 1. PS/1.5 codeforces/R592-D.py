n = int(input())
arr = []
for i in range(n):
    arr.append([0] + list(map(int, input().split())))
order = [0]*100000
# 링크드 리스트 구현? 해서 일렬로 세워서 계산? 3*2*100000
for i in range(n-1):
    
