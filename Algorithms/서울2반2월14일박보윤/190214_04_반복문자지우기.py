"""
4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
문제 내용
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
다음은 AAABBA에서 반복문자를 지우는 경우의 예이다.
CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
CAA 연속 문자 AA를 지운다.
C 1글자가 남았으므로 1을 리턴한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
#1 1
#2 4
#3 11

최초 작성 2019.02.14 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190214_04_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    # input
    s = input()

    # stack 만들기
    stack = ['0'] * len(s)
    top = 0

    # stack 이용
    for i in s:
        if i == stack[top-1]: # 반복 문자 체크
            top -= 1 # pop
        else:
            stack[top] = i
            top += 1 # push

    print("#{} {}".format(tc+1, top))