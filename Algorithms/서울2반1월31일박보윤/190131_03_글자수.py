""" 
4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
문제 내용
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.
파이썬의 경우 딕셔너리를 이용할 수 있다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어진다. 5≤N≤100, 10≤M≤1000, N≤M

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.01.31 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190131_03_input.txt", "r")

testcase = int(input())
for tc in range(1, testcase+1):
    # input
    str1 = input()
    str2 = input()

    # 글자수를 체크하기 위한 리스트 생성
    str1count = [0 for _ in range(len(str1))]

    # 문자열을 돌면서
    for s in str2:
        # 비교할 문자열도 한 번씩 체크
        for s2 in range(len(str1)):
            # 동일한 글자 발견시
            if s == str1[s2]:
                # 해당 글자가 몇 번 나왔는지 체크
                str1count[s2] += 1

    # max값 찾기
    mv = 0
    # 글자수 리스트를 돌면서
    for c in str1count:
        if c > mv:
            mv = c # max값 업데이트

    # 최종 답안 출력
    print("#%d %d" %(tc,mv))

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
