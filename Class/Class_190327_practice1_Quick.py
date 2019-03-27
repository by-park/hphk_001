"""
퀵정렬 연습문제

입력 예)
11 45 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0

2019.03.27 PBY
"""


def quickSort(l, r):
    if l < r:
        s = partition(l, r)
        quickSort(l, s-1)
        quickSort(s+1, r)

def partition(l, r):
    print("partition", A, "pivot", A[l])
    p = A[l] # 맨 앞을 피봇으로 삼는다
    i = l # 내 자리부터 오른쪽으로 가면 내 오른쪽이고
    j = r # 내가 맨 앞자리니까 끝에서부터 왼쪽으로 오면 내 왼쪽이라고 생각
    while i <= j: # i는 내 오른쪽, j는 내 왼쪽 부분을 담당하는 애니까 둘이 엇갈리면 끝나야한다. 왼쪽, 오른쪽 탐색이 각각 이루어진거다. 
        while A[i] <= p:
            #print(i, A[i], p, j)
            i += 1
            if i > j: break # 교재에 왜 이 부분 없지
        while A[j] >= p:
            if j == 0: break # 교재에 왜 이 부분은 없지
            j -= 1
        if i < j: # 어떤 경우에 i랑 j랑 같아짐? 서로 탐색하다가 한 지점에서 만나면, 바꿀 애를 못 ㅏㅈ은 것
            A[i], A[j] = A[j], A[i]
    print(A)
    A[l], A[j] = A[j], A[l]
    print(A)
    return j


"""
def partition(p, r):
    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
"""

if __name__ == "__main__":
    A = list(map(int, input().split()))
    quickSort(0, len(A)-1)
    print(A)
