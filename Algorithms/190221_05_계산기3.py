"""
[S/W 문제해결 기본] 6일차 - 계산기3
문제 내용
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
예를 들어
“3+(4+5)*6+7”
라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"345+6*+7+"
변환된 식을 계산하면 64를 얻을 수 있다.
문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.
이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.
피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.
총 10개의 테스트 케이스가 주어진다.
113
(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)
85
(4+8+4*(8*5*(7*(6*8)+3+(6+(3+7+1*7*5*4)*3)*2*3+5)+6+7*7)*4+2+9*4+7+2*3*(7*6*1*8)+9+9)

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.
#1 672676
#2 1974171
...

최초 작성 2019.02.21 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190221_05_input.txt", "r")

for tc in range(10):
    # input
    N = input()
    equation = input()

    # 1. 스택을 이용해서 후위 표기법으로 변경
    stack = [''] * int(N)
    post = ''
    top = -1

    # 우선순위 정리
    inner_priority = {'(': 0, '+': 1, '*': 2}
    outer_priority = {'(': 3, '+': 1, '*': 2}

    # 식의 각 토큰을 하나씩 확인하면서 스택에 넣는다.
    for token in equation:

        # 피연산자의 경우 후위 표기법으로 출력
        if token.isdigit():
            post += token

        # 연산자의 경우 스택에 쌓음
        else:
            # 닫는 괄호를 만나면 여는 괄호까지 스택에서 꺼내 후위표기법으로 이동
            if token == ")":
                while stack[top] != '(':
                    post += stack[top]
                    top -= 1
                top -= 1 # 마지막에 '(' 한 번 더 빼줌

            # 괄호 외 연산자들
            else:
                # 스택 내에 우선순위를 비교할 대상이 없는 경우, 본인이 앉음
                if top == -1:
                    top += 1
                    stack[top] = token
                    continue

                # 스택 내의 연산자와 현재 들어갈 토큰의 우선순위를 비교
                if inner_priority[stack[top]] < outer_priority[token]:
                    # 딱 눌러앉음
                    top += 1
                    stack[top] = token

                # 우선 순위가 높지 않은 경우
                else:
                    # 내가 앉을 수 있을 때까지 계속 비켜달라고 함
                    while inner_priority[stack[top]] >= outer_priority[token]:
                        post += stack[top] # 후위표기법으로 계속 보내줌
                        top -= 1
                        # 더 이상 비켜달라고 할 대상이 없으면
                        if top == -1:
                            break # while 문 탈출
                    # 내가 앉을 수 있게 되면 그때 스택에 토큰이 들어감
                    top += 1
                    stack[top] = token

    # 스택에 남은 것을 모두 후위 표기식으로 이동
    for res in range(top, -1, -1):
        post += stack[res]

    # 2. 스택을 이용해서 후위 표기법을 계산
    # 스택 초기화
    stack = [0] * len(post)
    top = -1

    # 저장한 후위 표기법을 돌면서 연산
    for token in post:

        # 피연산자의 경우 스택에 넣음
        if token.isdigit():
            top += 1
            stack[top] = int(token)

        # 연산자의 경우 스택을 이용해서 연산 (개수가 에러나는 경우는 없음)
        else:
            if token == "*":
                stack[top-1] = stack[top-1] * stack[top]
                top -= 1
            else:
                stack[top-1] = stack[top-1] + stack[top]
                top -= 1

    # output
    print("#{} {}".format(tc+1, stack[0]))