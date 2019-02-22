"""
4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
문제 내용
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
3 4 + .
Forth에서는 동작은 다음과 같다.
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
#1 84
#2 error
#3 168

최초 작성 2019.02.21 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190221_01_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    # input
    equation = input().split()

    # 후위 표기법을 위한 스택 초기화
    stack = [0] * len(equation)
    top = -1

    # 후위 표기법을 한 토큰씩 돌면서 진행
    for token in equation:

        # 피연산자인 경우 (숫자인 경우, 바로 스택에 넣음)
        if token.isdigit():
            top += 1
            stack[top] = int(token)

        # 연산자의 경우
        else:
            # 연산의 대상이 없는 경우 에러
            if top < 0:
                print("#{} error".format(tc + 1))
                break

            # 마지막 토큰이 들어온 경우
            elif token == ".":  # 혹시 처음부터 .인 경우가 있나? => 아니었다. 9/10 맞음
                # 마지막 토큰인데 숫자가 남아있는 경우 에러
                if top > 0:  # 혹시 숫자만 들어오는 경우가 있나? 숫자 숫자 . => 이거다! 숫자가 다 없어지지 않으면 에러!
                    print("#{} error".format(tc + 1))
                    break
                #  정상적으로 마지막 토큰을 만난 경우, 정답 출력
                else:
                    print("#{} {}".format(tc + 1, stack[top]))
                    break

            # 중간에 피연산자가 부족한 경우
            elif top < 1:
                print("#{} error".format(tc + 1))
                break

            # 연산자 중 +를 만난 경우, 스택을 활용
            elif token == "+":
                temp = stack[top - 1] + stack[top]
                top -= 1
                stack[top] = temp

            # 연산자 중 *를 만난 경우, 스택 활용
            elif token == "*":
                temp = stack[top - 1] * stack[top]
                top -= 1
                stack[top] = temp

            # 연산자 중 / 를 만난 경우, 소수점이 나오지 않게 //로 교체
            elif token == "/":
                temp = stack[top - 1] // stack[top]  # 나눗셈 소숫점 처리 안 해서 5/10 개 맞음
                top -= 1
                stack[top] = temp

            # 연산자 중 -를 만난 경우, 스택을 활용
            elif token == "-":
                temp = stack[top - 1] - stack[top]
                top -= 1
                stack[top] = temp

    # 후위 표기법을 다 돌았지만 .을 만나지 못한 경우 에러
    else:
        print("#{} error".format(tc + 1))  # 혹시 . 이 없는 경우가 있나? => 아니었다.

