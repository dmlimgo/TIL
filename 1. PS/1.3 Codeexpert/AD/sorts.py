def Qsort2(s, e):
    if start >= end: return
    pivot = end     # 맨 오른쪽에서 부터 시작
    target = start  # 맨 왼쪽에서 부터 시작

    for left in range(start, end+1):
        if nums[left] < nums[pivot]:    # 비교는 피봇과 왼쪽
            nums[left], nums[target] = nums[target], nums[left]  # 교환은 왼쪽과 타겟
            target += 1                 # 교환하고나면 target의 위치를 꼭 하나 올려주자
    nums[target], nums[pivot] = nums[pivot], nums[target]
    # 다시 재귀를 돌릴 때는 스타트는 그대로 end는 타겟보다 하나 작은 쪽으로
    QuickSort(start, target-1)
    # 오른쪽에 대해서는 이런식으로...
    QuickSort(target+1, end)

def Qsort(s, e):
    if s >= e: return
    t, p = s, e
    for l in range(s, e+1):
        if arr[l] < arr[p]:
            arr[l], arr[t] = arr[t], arr[l]
            t += 1
    arr[p], arr[t] = arr[t], arr[p]
    Qsort(s, t-1)
    Qsort(t+1, e)

def Msort(s, e):
    if s >= e: return
    m = (s+e) // 2
    Msort(s, m)
    Msort(m+1, e)
    i, j, k = s, m+1, s
    while i <= m and j <= e: # 왼쪽영역, 오른쪽영역을 나누어서 임시버퍼에 비교한 후 저장
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    while i <= m: # 왼쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= e: # 오른쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = arr[j]
        k += 1
        j += 1
