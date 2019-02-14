"""
4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
문제 내용
주어진 입력에서 괄호 {}, ()가 제대로 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 1
#2 1
#3 0

최초 작성 2019.02.14 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190214_02_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    # input
    s = input()

    # stack 만들기
    stack = [-1] * len(s)
    top = 0

    # 괄호
    bracket_l = ['(', '{']
    bracket_r = [')', '}']

    ans = 1
    # stack 이용
    for i in s:
        # 괄호 종류 하나씩 검사
        for b in range(2):
            # 여는 괄호를 만나면 스택에 넣음
            if i == bracket_l[b]:
                stack[top] = b
                top += 1
            elif i == bracket_r[b]:
                # 스택에 정상적으로 만난 경우
                if stack[top - 1] == b:
                    stack[top - 1] = -1  # 그 칸은 초기화
                    top -= 1
                # 여는 괄호가 맞지 않는 오류 찾기
                else:
                    ans = 0

    if top != 0:
        ans = 0
    print("#{} {}".format(tc+1,ans))