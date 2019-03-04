"""
[S/W 문제해결 기본] 9일차 - 사칙연산
사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다. 아래는 식 “(9/(6-4))*3”을 이진 트리로 표현한 것이다.
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과를 사용해서 해당 연산자를 적용한다.
사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진트리가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.
단, 중간 과정에서의 연산은 실수 연산으로 하되, 최종 결과값이 정수로 떨어지지 않으면 정수부만 출력한다.
위의 예에서는 최종 결과값이 13.5이므로 13을 출력하면 된다.

[제약 사항]
정점의 총 수 N은 1≤N≤1000.

[입력]
각 테스트 케이스의 첫 줄에는 각 케이스의 트리가 갖는 정점의 총 수 N(1≤N≤1000)이 주어진다. 그 다음 N줄에 걸쳐 각각의 정점 정보가 주어진다.
정점이 단순한 수이면 정점번호와 해당 양의 정수가 주어지고, 정점이 연산자이면 정점번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호가 차례대로 주어진다.
정점번호는 1부터 N까지의 정수로 구분된다. 입력에서 정점 번호를 매기는 특별한 규칙은 없으나, 루트 정점의 번호는 반드시 1이다.
입력에서 이웃한 수나 연산자는 모두 공백으로 구분된다.
위의 예시에서, 숫자 4가 7번 정점에 해당하면 “7 4”으로 주어지고, 연산자 ‘/’가 2번 정점에 해당하면 두 자식이 각각 숫자 9인 4번 정점과 연산자 ‘-’인 5번 정점이므로 “2 / 4 5”로 주어진다.
총 10개의 테스트 케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다. 답은 항상 정수값으로 기록한다.

2019.03.04 PBY 최초작성
"""

import sys
sys.stdin = open('C:/Users/student/Documents/week2/day1/Algorithms/190305_05_input.txt', 'r')


def postorder(start):
    if len(binary_tree[start]) > 1:
        postorder(int(binary_tree[start][1]))
        postorder(int(binary_tree[start][2]))
        stack.append(binary_tree[start][0])
    else:
        stack.append(binary_tree[start][0])


for tc in range(10):

    # 정점의 수가 주어진다.
    nodes = int(input())

    # 이진 트리 만들기
    binary_tree = [0 for __ in range(nodes+1)]

    # 이진 트리 채우기
    for n in range(nodes):
        cur_input = input().split()
        binary_tree[int(cur_input[0])] = cur_input[1:] # 어차피 조회를 목적으로 한 순회라서 주소값이 와도 상관 없음

    # 후위 순회 하면서 스택에 넣기
    stack = []
    postorder(1)

    # 스택을 돌면서 연산하기 (숫자는 항상 2개씩 밖에 없다)
    i = 0
    while len(stack) != 1:
        if stack[i] in ['-', '*', '+', '/']:
            if stack[i] == '-':
                stack[i] = int(stack[i-2]) - int(stack[i-1])
            elif stack[i] == '*':
                stack[i] = int(stack[i-2]) * int(stack[i-1])
            elif stack[i] == '+':
                stack[i] = int(stack[i-2]) + int(stack[i-1])
            else:
                stack[i] = int(stack[i-2]) // int(stack[i-1])
            stack.pop(i-2)
            stack.pop(i-2) # i-1을 빼려면 한 번 더 빼야함
            i -= 2
        i += 1

    # 결과 출력
    print("#%d %d" %(tc+1, stack[0]))