# scoville_len = 0
# scoville = []
# def heapify(i):
#     global scoville, scoville_len
#     left = i*2
#     right = i*2+1
#     small = i
#     if left <= scoville_len-1 and scoville[left] < scoville[small]:
#         small = left
#     if right <= scoville_len-1 and scoville[right] < scoville[small]:
#         small = right
#     if small != i:
#         scoville[small], scoville[i] = scoville[i], scoville[small]
#         heapify(small)
# def heapSort():
#     global scoville_len
#     for i in range(scoville_len//2, 0, -1):
#         heapify(i)
# def delete():
#     global scoville, scoville_len
#     scoville[1], scoville[-1] = scoville[-1], scoville[1]
#     minVal = scoville.pop()
#     scoville_len -= 1
#     heapify(1)
#     return minVal
# def insert(n):
#     global scoville, scoville_len
#     scoville.append(n)
#     scoville_len += 1
#     i = scoville_len-1
#     while 1 < i:
#         parent = i//2
#         if scoville[parent] > scoville[i]:
#             scoville[parent], scoville[i] = scoville[i], scoville[parent]
#             i = parent
#         else:
#             break
# def solution(arr, K):
#     global scoville, scoville_len
#     scoville = [0] + arr
#     answer = 0
#     scoville_len = len(scoville)
#     heapSort()
#     while scoville[1] < K and scoville_len != 2:
#         first = delete()
#         second = delete()
#         mixed = first + second*2
#         insert(mixed)
#         answer += 1
#     if scoville[1] >= K:
#         return answer
#     else:
#         return -1
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    scoville_len = len(scoville)
    while scoville[0] < K and scoville_len != 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mixed = first + 2*second
        heapq.heappush(scoville, mixed)
        scoville_len -= 1
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1