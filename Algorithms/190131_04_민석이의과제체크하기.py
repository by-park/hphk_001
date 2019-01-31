""" 
민석이의 과제 체크하기
문제 내용
민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.
민석이는 처음으로 과제를 내었다.
그리고 제출한 사람의 목록을 받았다.
수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.
과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 수강생의 수를 나타내는 정수 N(2≤N≤100)과 과제를 제출한 사람의 수를 나타내는 정수 K(1≤K≤N)가 공백으로 구분되어 주어진다.
두 번째 줄에는 과제를 제출한 사람의 번호 K개가 공백으로 구분되어 주어진다. 번호는 1이상 N이하의 정수이며 같은 번호가 두 번 이상 주어지는 경우는 없다.

[출력]
각 테스트 케이스마다 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력한다.

최초 작성 2019.01.31 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190131_04_input.txt", "r")

# 더 짧게 짜보기
testcase = int(input())
for tc in range(1, testcase+1):
    ns, hs = input().split()
    hsname = list(map(int, input().split()))

    # 숙제 낸 사람 체크할 리스트
    nhsname = [0 for _ in range(int(ns))]

    # 숙제 낸 사람 명단을 돌면서
    for i in hsname:
        nhsname[i-1] = 1

    # 숙제 안 낸 사람 (0으로 표시된 사람만) 출력
    ans = ''
    for i in range(int(ns)):
        if nhsname[i] == 0:
            ans += str(i+1) + ' '
    print("#%d %s" %(tc, ans))

"""
# 더 짧게 짜보기
testcase = int(input())
for tc in range(1, testcase+1):
    ns, hs = list(map(int, input().split()))
    hsname = list(map(int, input().split()))

    print("#%d" % tc, end=" ")
    for i in range(1, ns+1):
        for j in hsname:
            if i == j:
                break
        else:
            print(i, end=" ")
    print()
"""

"""
# 이전 코드
testcase = int(input())
for tc in range(1, testcase+1):
    ns, hs = list(map(int, input().split()))
    hsname = list(map(int, input().split()))

    # 숙제 낸 사람 체크할 리스트
    nhsname = [0 for _ in range(ns)]

    # 1~N 수강생 번호를 돌면서
    for i in range(1, ns+1):
        # 숙제 낸 사람 명단을 체크
        for j in hsname:
            if i == j: # 숙제 낸 사람을 리스트에 체크
                nhsname[i-1] = 1

    # 정답 출력
    print("#%d" %tc, end=" ")
    # 숙제 안 낸 사람 (0으로 표시된 사람만) 출력
    for i in range(len(nhsname)):
        if nhsname[i] == 0:
            print(i+1, end = " ")
    print()
"""

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
