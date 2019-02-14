"""
4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기
문제 내용
어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.
그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다. N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.
10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 직사각형 종이가 모자라는 경우는 없다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.02.14 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190214_01_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    N = int(input())

    # 제한 시간 초과 방지를 위한 Memoization
    memo = [0] * ((N // 10) + 1)

    def fillfloor(N):
        if N >= 20:
            # fillfloor(N)에 3가지 경우 10짜리, 20짜리 1개, 10짜리 가로로 붙인 거 1개
            if memo[N//10] > 0:
                result = memo[N//10]
            else:
                result = fillfloor(N-10) + fillfloor(N-20) + fillfloor(N-20)
                memo[N//10] = result
            return result
        elif N == 10: # 남은 칸이 10개면 1가지 경우밖에 없음
            return 1
        else: # N = 0
            return 1 # 다 붙이면 가능한 경우 한 개 증가

    print("#{} {}".format(tc+1, fillfloor(N)))


# 20 남았을 때 20 크기 붙여서 끝내는 경우 있어야 하니까 elif N==10: 조건까지만 하고 끝내면 안 된다!

# 시간제한 초과 난 원래 코드
"""
testcase = int(input())
for tc in range(testcase):
    N = int(input())
    
    def fillfloor(N):
        if N >= 20:
            # fillfloor(N)에 3가지 경우 10짜리, 20짜리 1개, 10짜리 가로로 붙인 거 1개
            return fillfloor(N-10) + fillfloor(N-20) + fillfloor(N-20)
        elif N == 10: # 남은 칸이 10개면 1가지 경우밖에 없음
            return fillfloor(N-10)
        else: # N = 0
            return 1 # 다 붙이면 가능한 경우 한 개 증가

    print("#{} {}".format(tc+1, fillfloor(N)))
"""