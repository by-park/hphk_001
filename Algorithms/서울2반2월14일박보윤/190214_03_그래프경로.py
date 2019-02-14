"""
4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
문제 내용
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
3
6 5
1 4
1 3
2 3
2 5
...

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 1
#2 1
#3 1

최초 작성 2019.02.14 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190214_03_input.txt", "r")

testcase = int(input())
for tc in range(testcase):

    # input
    V, E = map(int, input().split())
    G = [[0 for _ in range(V+1)] for __ in range(V+1)]
    visited = [0]*(V+1)
    # G 채우기
    for lines in range(E):
        nodes = list(map(int, input().split()))
        G[nodes[0]][nodes[1]] = 1 # [출발][도착]
    S, T = map(int, input().split())

    # stack
    stack = [0] * V
    top = 0

    # DFS 구현
    # next 지점 찾는 함수
    def findnext(v):
        for i in range(V+1):
            if G[v][i] and not visited[i]:
                return i
        return 0

    # 시작 지점 S
    v = S
    visited[v] = 1
    ans = 0

    while v:
        w = findnext(v)
        if w == T: # 경로가 존재하면 나가기
            ans = 1
            break

        if w: # 다음 경로가 존재하면 이어서 탐색
            stack[top] = v
            top += 1

        while w:
            visited[w] = 1
            stack[top] = w
            top += 1

            # 다음 경로 탐색
            v = w
            w = findnext(v)

            if w == T: # 경로가 존재하면 나가기
                ans = 1
                break

        # 경로 탐색 후 stack에서 빼기
        if top > 0:
            v = stack[top-1]
            top -= 1
        else: # underflow 처리
            v = 0

    print("#{} {}".format(tc+1, ans))