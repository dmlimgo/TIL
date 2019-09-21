import time
start = time.time()

arr = list(range(1000,1,-1))
heap = [0]
heap_len = 1

def parent(index):
    return index//2
def leftchild(index):
    return index*2
def rightchild(index):
    return index*2 + 1
def insert(n):
    global heap_len
    heap.append(n)
    heap_len += 1
    i = heap_len-1
    while i > 1:
        p = parent(i)
        if heap[i] < heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break
def delete():
    global heap_len
    heap[1], heap[-1] = heap[-1], heap[1]
    heap.pop()
    heap_len -= 1
while arr:
    n = arr.pop(0)
    insert(n)
print(heap[:10])
print(time.time()-start)

start = time.time()
narr = [0] + list(range(1000,1,-1))
arr_len = len(narr)
def minHeapify(i):
    left = leftchild(i)
    right = rightchild(i)
    smallest = i
    if left <= arr_len-1 and narr[left] < narr[smallest]:
        smallest = left
    if right <= arr_len-1 and narr[right] < narr[smallest]:
        smallest = right
    if smallest != i:
        narr[i], narr[smallest] = narr[smallest], narr[i]
        minHeapify(smallest)
for i in range(arr_len//2, 0, -1):
    minHeapify(i)
print(narr[:10])
print(time.time()-start)

