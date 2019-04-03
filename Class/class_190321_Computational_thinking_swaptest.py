import math

def stupid(start, end):
    print(A)
    print('start:', start, 'end:', end)
    if end-start ==1:
        if A[start] > A[end]:
            A[start], A[end] = A[end], A[start]
    else: # end-start == 1: 이면 여기로 넘어오면 안 된다!!!!!!!!!
        newend = math.ceil((start+2*(end+1))/3)
        stupid(start, newend-1)
        stupid(start + end-newend+1, end)
        stupid(start, newend-1)

A = [9, 7, 3, 4, 2]
stupid(0, 4)
print(A)

"""
[9, 7, 3, 4, 2]
start: 0 end: 5
[9, 7, 3, 4, 2]
start: 0 end: 3
[9, 7, 3, 4, 2]
start: 0 end: 2
[9, 7, 3, 4, 2]
start: 0 end: 1
[7, 9, 3, 4, 2]
start: 1 end: 2
[7, 3, 9, 4, 2]
start: 0 end: 1
[3, 7, 9, 4, 2]
start: 1 end: 3
[3, 7, 9, 4, 2]
start: 0 end: 2
[3, 7, 9, 4, 2]
start: 0 end: 1
[3, 7, 9, 4, 2]
start: 0 end: 0
[3, 7, 9, 4, 2]
start: 0 end: 0

maximum recursion depth exceeded in comparison
"""
