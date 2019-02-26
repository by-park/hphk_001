"""
5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.02.26 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190226_02_input.txt", "r")

T = int(input())
for tc in range(T):
    # 필요한 input
    N = int(input())
    miro = [[0 for j in range(N)] for i in range(N)]
    for row in range(N):
        temp_input = input()
        for col in range(N):
            miro[row][col] = int(temp_input[col])

    # BFS 구현을 위한 초기 변수
    delta1 = [-1, 0, 1, 0]
    delta2 = [0, 1, 0, -1]
    Q = [0] * N * N * N
    front = 0
    rear = 0

    # 시작점 위치 파악하기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)
    Q[rear] = start

    # while문 종료 조건과 결과 출력을 위한 탐색의 깊이 변수
    depth = -1
    check = 0

    # BFS 구현
    while check == 0:
        # 매번 큐를 업데이트 할 때마다 깊이를 하나씩 증가시킴
        depth += 1

        # 다음 자식 노드가 있는지 확인하기 위한 임시 변수
        rear_temp = rear

        # 4개의 위치를 찾아가면서 도착점 3을 만날 때까지 계속 진행
        for idx in range(front, rear+1): # 지금 queue에 있는 애들을 다 돌면서

            front += 1 # 돌 때마다 하나씩 큐에서 빼줌 - 이미 간 애들은 또 안 갈 거니까 큐에서 빠짐

            # 상하좌우 모든 방향을 확인
            for direction in range(4): # 4 방향을 확인
                nextx = Q[idx][0] + delta1[direction]
                nexty = Q[idx][1] + delta2[direction]

                # 판을 넘어서지 않았고, 벽이 아닐 때
                if -1 < nextx < N and -1 < nexty < N and miro[nextx][nexty] != 1:

                    # 이동할 곳이 도착점이라면 while문을 종료
                    if miro[nextx][nexty] == 3:
                        check = 1

                    # 다음 자식 노드들을 큐의 뒤에 넣어줌
                    rear += 1
                    Q[rear] = (nextx, nexty)

                    # 지나간 곳은 1로 체크해줌
                    miro[nextx][nexty] = 1

        # 다음 자식 노드가 존재하지 않으면 while문 종료 (3으로 갈 수 없는 경우)
        if rear_temp == rear:
            check = 1
            depth = 0

    print("#{} {}".format(tc+1, depth))


# 런타임 에러: visited 변수를 사용 안 하는 바람에 탐색시 자꾸 뒤로 돌아가서 런타임 에러가 났다.
