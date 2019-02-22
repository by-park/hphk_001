"""
4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
문제 내용
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

최초 작성 2019.02.21 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190221_02_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    # input
    N = int(input())

    # miro 배열 생성
    miro = []
    for _ in range(N):
        miro.append(input())

    # miro를 복사한 visited 생성 (miro가 string이라서 바로 visited 표시를 할 수 없었다)
    visited = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            visited[i][j] = int(miro[i][j])

    # 스택 초기화
    stack = [0] * N * N
    top = -1

    # 이동을 위한 델타
    d1 = [0, -1, 0, 1]
    d2 = [-1, 0, 1, 0]

    # 시작점 2 의 위치 찾기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 2:
                top += 1
                stack[top] = (i, j)

    # 3을 만나지 못한 경우 출력할 정답을 0으로 초기화
    ans = 0

    # 시작점 2 부터 시작해서 이동하기
    while top > -1:

        # 4 가지 방향을 모두 확인
        for delta in range(len(d1)):
            # 다음으로 갈 수 있는 좌우 방향이 벽인지 판단 + 방문 했는지 판단
            if N-1 >= stack[top][1] + d2[delta] >= 0 and visited[stack[top][0]][stack[top][1] + d2[delta]] != 1:
                # 3을 만나면 정답이므로 break
                if visited[stack[top][0]][stack[top][1] + d2[delta]] == 3:
                    ans = 1
                    top = -1 # while문 종료 조건
                    break # for 문 종료
                # 벽이 아닌 경우 다음 갈 곳을 탐색
                elif visited[stack[top][0]][stack[top][1] + d2[delta]] == 0:
                    top += 1
                    stack[top] = (stack[top - 1][0], stack[top - 1][1] + d2[delta])
                    visited[stack[top][0]][stack[top][1]] = 1
                    break

            # 다음으로 갈 수 있는 상하 방향이 벽인지 판단 + 방문 했는지 판단 (이걸 elif로 잡으면 2를 만나는 경우 때문에 들어오지 못한 때가 있다)
            if N-1 >= stack[top][0] + d1[delta] >= 0 and visited[stack[top][0]+d1[delta]][stack[top][1]] != 1:
                # 3을 만나면 정답이므로 break
                if visited[stack[top][0] + d1[delta]][stack[top][1]] == 3:
                    ans = 1
                    top = -1 # while 종료 조건
                    break
                # 벽이 아닌 경우 다음 갈 곳을 탐색
                elif visited[stack[top][0] + d1[delta]][stack[top][1]] == 0:
                    top += 1
                    stack[top] = (stack[top - 1][0] + d1[delta], stack[top - 1][1])
                    visited[stack[top][0]][stack[top][1]] = 1
                    break
        # for문을 break하지 못하면 좌우 상하 다 못가기 때문에 pop을 한다.
        else:
            top -= 1

    # output
    print("#{} {}".format(tc+1,ans))

