T = int(input())

for tc in range(T):
    N, K = list(map(int, input().split()))
    fruits = []
    for _ in range(N):
        fruits.append(list(map(int, input().split())))

    minvalue = 100*N*2

    # start점 잡기 (사각형처럼 해당 영역의 시작점이 모여있음)
    for i in range(N-K+1):
        for j in range(N-K+1):
            left, right = 0, 0
            # 왼쪽 대각선 합 구하기
            for k in range(K):
                left += fruits[i + k][j + K-1 - k]
            # 오른쪽 대각선 합 구하기
            for k in range(K):
                right += fruits[i + k][j + k]
            # 최소값 비교
            if minvalue > abs(left-right):
                minvalue = abs(left-right)

    print("#%d %d" %(tc+1, minvalue))
