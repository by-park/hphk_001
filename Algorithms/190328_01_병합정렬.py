def merge_sort(m):
    global cnt
    if len(m) == 1: return m[0]
    if len(m) == 2:
        if m[0] > m[1]:
            cnt += 1
        return max(m[0], m[1]) # 어차피 두개인 경우 이걸 비교하라고 merge 함수 호출 안 함
    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])

    # 여러 개가 오면 그거 중에 max를 비교
    if left > right:
        cnt += 1
    return max(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    result = [0] * N
    sorted_numbers = merge_sort(numbers)
    print("#%d %d %d" %(tc, sorted(numbers)[N//2], cnt))

"""
# 1초 더 단축 가능
# while문 따로 있고,
if idxL < lenL:
    arr[i:] = left[idxL:]
    # 덧붙일 때 증가시킴. 이 경우 확실하게 right가 더 작은 경우니까! 
    cnt += 1
if idxR < lenR:
    arr[i:] = right[idxR:]
#
"""

"""
def merge_sort(m):
    global cnt
    if len(m) == 1: return m
    if len(m) == 2:
        if m[0] > m[1]:
            cnt += 1
            m[0], m[1] = m[1], m[0]
        return m # 어차피 두개인 경우 이걸 비교하라고 merge 함수 호출 안 함
    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])
    
    # 병합을 순차적으로 부르면서 left와 right 비교
    if left[-1] > right[-1]:
        cnt += 1
    idx = 0; leftidx = 0; rightidx = 0
    leftN = len(left); rightN = len(right)
    while leftidx < leftN or rightidx < rightN:
        if leftidx < leftN and rightidx < rightN:
            if left[leftidx] <= right[rightidx]:
                result[idx] = left[leftidx]
                idx += 1
                leftidx += 1
            else:
                result[idx] = right[rightidx]
                idx += 1
                rightidx += 1
        elif leftidx < leftN:
            result[idx] = left[leftidx]
            idx += 1
            leftidx += 1
        elif rightidx < rightN:
            result[idx] = right[rightidx]
            idx += 1
            rightidx += 1
    return result[:idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    result = [0] * N
    sorted_numbers = merge_sort(numbers)
    print("#%d %d %d" %(tc, sorted_numbers[N//2], cnt))
"""

"""
# 시간초과
def merge_sort(m):
    if len(m) == 1: return m
    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])

    return merge(left, right)

def merge(left, right):
    global cnt
    # 병합을 순차적으로 부르면서 left와 right 비교
    if left[-1] > right[-1]:
        cnt += 1
    idx = 0; leftidx = 0; rightidx = 0
    leftN = len(left); rightN = len(right)
    while leftidx < leftN or rightidx < rightN:
        if leftidx < leftN and rightidx < rightN:
            if left[leftidx] <= right[rightidx]:
                result[idx] = left[leftidx]
                idx += 1
                leftidx += 1
            else:
                result[idx] = right[rightidx]
                idx += 1
                rightidx += 1
        elif leftidx < leftN:
            result[idx] = left[leftidx]
            idx += 1
            leftidx += 1
        elif rightidx < rightN:
            result[idx] = right[rightidx]
            idx += 1
            rightidx += 1
    return result[:idx]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    result = [0] * N
    sorted_numbers = merge_sort(numbers)
    print("#%d %d %d" %(tc, sorted_numbers[N//2], cnt))
"""

"""
# 시간초과
def merge_sort(m):
    if len(m) == 1: return m
    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])

    return merge(left, right)

def merge(left, right):
    global cnt
    # 병합을 순차적으로 부르면서 left와 right 비교
    if left[-1] > right[-1]:
        cnt += 1
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) >0 :
            result.append(right.pop(0))
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    sorted_numbers = merge_sort(numbers)
    print("#%d %d %d" %(tc, sorted_numbers[N//2], cnt))
"""

