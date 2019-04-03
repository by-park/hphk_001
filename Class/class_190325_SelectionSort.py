"""
selection sort
"""

# 지금까지 정렬된 부분을 알려주고, 나머지 부분에서 최소값을 찾아 자리를 바꾸도록 한다.
def SelectionSort(sorted_length):
    global N
    # 종료 시점
    if sorted_length == N-1:
        return
    minidx = sorted_length
    for item in range(sorted_length+1, N):
        if A[minidx] > A[item]:
            minidx = item
    A[sorted_length], A[minidx] = A[minidx], A[sorted_length]
    SelectionSort(sorted_length+1)


# 배열이 들어오면
A = [27, 10, 3, 14, 2, 23]
N = len(A)

SelectionSort(0)
print(A)
