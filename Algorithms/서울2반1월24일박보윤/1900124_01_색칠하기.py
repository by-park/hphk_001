""" 
4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
문제 내용
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
주어진 정보에서 같은 색인 영역은 겹치지 않는다.

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
2
2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
color = 1 (빨강), color = 2 (파랑)

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.01.24 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190124_01_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    nrow = int(input())
    # 10 x 10 격자 만들기
    grid = [[0 for _ in range(10)] for i in range(10)]

    for row in range(nrow):
        colors = list(map(int, input().split()))

        # 빨강, 파랑 체크할 필요 없음 - 문제 상 겹치는 것 없다고 했음
        for i in range(10):
                for j in range(10):
                    if colors[0] <= i <= colors[2] and colors[1] <= j <= colors[3]:
                        grid[i][j] += 1

    # 2이면 보라색으로 판단
    count = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] >= 2:
                count += 1
    print("#%d %d" % (tc+1, count))

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
