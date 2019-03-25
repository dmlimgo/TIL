import sys
sys.stdin = open('d4_input.txt')

# def visit(num):
#     global vary
#     if num not in eaten:
#         eaten[num] = 1
#         vary += 1
#     else:
#         eaten[num] += 1
#
# def unvisit(num):
#     global vary
#     eaten[num] -= 1
#     if eaten[num] == 0:
#         vary -= 1
#
# N, d, k, c = map(int, input().split())
# arr = []
# for n in range(N):
#     arr.append(int(input()))
# maxval = 0
#
# eaten = [0 for _ in range(d+1)]
# plate = arr[0:k] + [c]
#
# vary = 0
# for sushi in plate:
#     visit(sushi)
# if maxval < vary:
#     maxval = vary
# for i in range(N):
#     visit(arr[k])
#     unvisit(arr[0])
#     print(eaten)
#     if maxval < vary:
#         maxval = vary
#     arr.append(arr.pop(0))
# print(maxval)




#----
# eat = arr[0:k] + [c]
# max = len(set(eat))
# for i in range(N):
#     eat.pop(0)
#     if i+k >= N:
#         index = (i+k) % N
#         eat.append(arr[index])
#     else:
#         eat.append(arr[i+k])
#     if max < len(set(eat)):
#         max = len(set(eat))
# print(max)



N, d, k, c = map(int, input().split())
arr = []
for n in range(N):
    arr.append(int(input()))
eat = arr[0:k]
maxval = len(set(eat + [c]))
for i in range(N):
    eat.pop(0)
    eat.append(arr[k])
    length = len(set(eat + [c]))
    if maxval < length:
        maxval = length
    arr.append(arr.pop(0))
print(maxval)




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
