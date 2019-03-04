import sys
sys.stdin = open('d4_input.txt')

N, d, k, c = map(int, input().split())
arr = []
for n in range(N):
    arr.append(int(input()))
max = 0

eat = arr[0:k] + [c]
max = len(set(eat))
for i in range(N):
    eat.pop(0)
    if i+k >= N:
        index = (i+k) % N
        eat.append(arr[index])
    else:
        eat.append(arr[i+k])
    if max < len(set(eat)):
        max = len(set(eat))
print(max)



#-----
# eat = arr[0:k] + [c]
# max = len(set(eat))
# for i in range(N):
#     eat.pop(0)
#     eat.append(arr[k])
#     if max < len(set(eat)):
#         max = len(set(eat))
#     arr = arr[1:] + [arr[0]]
# print(max)




#-----
# i = 0
# while True:
#     if i >= N:
#         break
#     eat = len(set(arr[0:k] + [c]))
#     if max < eat:
#         max = eat
    # print(arr[i+k-1], c)
    # print(arr[0], c)
    # if arr[0] == c:
    #     arr = arr[k+1:] + arr[:k+1]
    #     N -= k - 1
#     arr = [arr[-1]] + arr[0:-1]
#     i += 1
# print(max)
