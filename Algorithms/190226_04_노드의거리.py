"""
5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
문제 내용
V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.02.26 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190226_04_input.txt", "r")


T = int(input())
for tc in range(T):

    # 필요한 input
    V, E = list(map(int,input().split()))
    lines = [[0 for j in range(V)] for i in range(V)]
    for row in range(E):
        temp = input().split()
        lines[int(temp[0])-1][int(temp[1])-1] = 1
        lines[int(temp[1])-1][int(temp[0])-1] = 1
    S, G = list(map(int, input().split()))

    # 방문 체크와 큐 구현을 위한 초기화
    visited = [0 for i in range(V)]
    Q = [0] * V * V * V
    front = -1; rear = -1

    # 시작점을 먼저 큐에 넣어줌
    front += 1; rear += 1
    Q[rear] = S
    visited[S-1] = 1

    # while문 종료 변수와 최단 거리 체크를 위한 변수
    depth = 0
    check = 0

    # BFS로 인접한 노드들 탐색
    while check == 0:

        # BFS를 한 레벨씩 갈 때마다 출력을 위해 깊이 저장
        depth += 1

        # 매번 큐를 확인할 때마다 다음 자식이 있는지 새로 확인
        node = 0

        # 현재 부모 큐에 있는 모든 노드들을 확인하면서
        for item in Q[front:rear+1]:

            # 이미 방문한 큐 내의 정점은 꺼내준다고 생각한다.
            front += 1

            # 자식 노드들을 모두 큐에 넣어줌
            for col in range(V):

                # 연결이 되어있고, 아직 방문하지 않은 곳일 때
                if lines[item-1][col] == 1 and not visited[col]:

                    # 도착 노드면 while문 종료
                    if col + 1 == G:
                        check = 1

                    # 도착 노드가 아니면 queue뒤에 새롭게 추가
                    rear += 1
                    Q[rear] = col + 1
                    visited[col] = 1

                    # 자식 노드 한 개 이상 존재함
                    node = 1

        # 아직 도착 지점이 아니더라도 더 갈 다음 자식 노드가 없는 경우 while문 종료
        if node == 0:
            check = 1
            depth = 0 # *** 이건 문제에 명세로 없었지만 넣어줘야 런타임 에러가 안 뜬다.

    print("#{} {}".format(tc+1,depth))


"""
런타임 에러가 굉장히 많이 났는데, 갈 수 없는 노드일 때 depth = 0 초기화가 없었기 때문이 아니라 
단순히 visited 배열을 사용하지 않았기 때문이었다....
논리적 사고를 잘하자....
"""
