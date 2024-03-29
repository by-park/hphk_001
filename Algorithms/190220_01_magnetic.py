"""
[S/W 문제해결 기본] 5일차 - Magnetic
문제 내용
테이블 위에 자성체들이 놓여 있다.
자성체들은 성질에 따라 색이 부여되는데, 푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고, 붉은 자성체의 경우 S극에 이끌리는 성질이 있다.
아래와 같은 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때, 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
아래는 자성체들이 놓여 있는 테이블을 위에서 바라본 모습이다.
A로 표시된 붉은 자성체의 경우 S극에 이끌리면서 테이블 아래로 떨어지게 된다.
B로 표시된 푸른 자성체의 경우 N극에 이끌리면서 테이블 아래로 떨어지게 된다.
나머지 자성체들은 서로 충돌하며, 교착 상태에 빠져 움직이지 않게 된다.
D로 표시된 자성체들에서 알 수 있듯 한 쪽 방향으로 움직이는 자성체의 개수가 많더라도 반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태에 빠져 움직이지 않는다.
D로 표시된 자성체들과 같이 셋 이상의 자성체들이 서로 충돌하여 붙어 있을 경우에도 하나의 교착 상태로 본다.
C와 D는 좌우로 인접하여 있으나 각각 다른 교착 상태로 판단하여 2개의 교착 상태로 본다.
E의 경우와 같이 한 줄에 두 개 이상의 교착 상태가 발생할 수도 있다.
F의 경우 각각 다른 교착상태로 판단하여 2개의 교착상태로 본다.
위의 예시의 경우 테이블 위에 남아있는 교착상태는 7개이므로 7를 반환한다.

[제약 사항]
자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.
테이블의 크기는 100x100으로 주어진다. (예시에서는 설명을 위해 7x7로 주어졌음에 유의)

[입력]
각 테스트 케이스의 첫 번째 줄에는 정사각형 테이블의 한 변의 길이가 주어진다. 그리고 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트 케이스가 주어진다.
1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며 테이블의 윗 부분에 N극이 아랫 부분에 S극이 위치한다고 가정한다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 교착 상태의 개수를 출력한다.

최초 작성 2019.02.20 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190220_01_input.txt", "r")

# 속도 줄이기 2

for tc in range(10):
    # input
    N = int(input())
    table = []
    for row in range(N):
        table.append(input())

    # 교착 상태 개수 체크
    count = 0

    # 테이블의 왼쪽 부터 차례로 돌면서
    for i in range(0, N*2, 2):

        # 스택 변수를 초기화
        stack = 0

        # 매 세로 줄을 스택처럼 확인하도록 할 것
        for j in range(N):

            # 현재 위치가 1 자성체면 스택에 넣어줌 (아래 방향으로 잡아당기는 힘)
            if table[j][i] == '1':
                stack = 1

            # 현재 위치가 2 자성체면 이전에 1이 있어야 교착이 가능함 (위로 잡아당기는 힘)
            elif table[j][i] == '2':
                if stack == 1:
                    stack = 0 # 교착 상태 만들면 스택을 비워줌
                    count += 1 # 교착 상태를 체크

    # 출력
    print("#{} {}".format(tc+1, count))



"""
# 속도 줄이기

for tc in range(10):
    # input
    N = int(input())
    table = []
    for row in range(N):
        table.append(input().split())

    # 교착 상태 개수 체크
    count = 0

    # 테이블의 왼쪽 부터 차례로 돌면서
    for i in range(N):

        # 스택 변수를 초기화
        stack = 0

        # 매 세로 줄을 스택처럼 확인하도록 할 것
        for j in range(N):

            # 현재 위치가 1 자성체면 스택에 넣어줌 (아래 방향으로 잡아당기는 힘)
            if table[j][i] == '1':
                stack = 1

            # 현재 위치가 2 자성체면 이전에 1이 있어야 교착이 가능함 (위로 잡아당기는 힘)
            elif table[j][i] == '2':
                if stack == 1:
                    stack = 0 # 교착 상태 만들면 스택을 비워줌
                    count += 1 # 교착 상태를 체크

    # 출력
    print("#{} {}".format(tc+1, count))
    
"""


"""
최초 제출 코드

for tc in range(10):
    N = int(input())
    table = []
    # table = [[] for _ in range(N)]
    for row in range(N):
#        table[row] = list(map(int, input().split()))
        table.append(list(map(int, input().split())))

    count = 0 # 교착상태 개수
    # 왼쪽 부터 차례로 돌면서
    for i in range(N):
        stack = 0 # 이걸 잘못 넣어서 아까 오류남
        # 스택처럼 확인할 수 있도록
        for j in range(N):
            if table[j][i] == 1:
                stack = 1
            elif table[j][i] == 2:
                if stack == 1:
                    count += 1
                    stack = 0
    print("#{} {}".format(tc+1, count))
"""

# stack = 0 초기화 부분을 for문 안에 넣지 않고 for문 밖에 넣어버려서
# 초기화가 안 되는 바람에 정답보다 항상 더 큰 수가 나왔다.