"""
숫자 배열 회전
문제 내용
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

[제약 사항]
N은 3 이상 7 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
다음 N 줄에는 N x N 행렬이 주어진다.

[출력]
출력의 첫 줄은 '#t'로 시작하고,
다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)


최초 작성 2019.02.27 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190227_01_input.txt", "r")

T = int(input())

for tc in range(T):
    # input
    rows = int(input())
    array = []
    for row in range(rows):
        array.append(input().split())

    # 90도 출력
    ans = [['' for _ in range(3)] for __ in range(len(array[0]))] # 90, 180, 270 을 넣을 곳
    for col in range(len(array[0])):
        for row in range(rows-1, -1, -1):
            ans[col][0] += array[row][col] # 문자열 합치기

    # 180도 출력
    for row in range(rows-1, -1, -1):
        ans[rows-1-row][1] = ''.join(array[row][::-1])

    # 270도 출력
    for col in range(len(array[0])-1, -1, -1):
        for row in range(rows):
            ans[rows-1-col][2] += array[row][col]

    print("#{}".format(tc+1))
    for row in range(len(ans)):
        print(' '.join(ans[row]))

"""
10개중 8개 맞음
NXN이 아닌가...?
"""

"""
T = int(input())

for tc in range(T):
    # input
    rows = int(input())
    array = []
    for row in range(rows):
        array.append(input().split())

    # 90도 출력
    ans = [['' for _ in range(3)] for __ in range(rows)] # 90, 180, 270 을 넣을 곳
    for col in range(rows):
        for row in range(rows-1, -1, -1):
            ans[col][0] += array[row][col] # 문자열 합치기

    # 180도 출력
    for row in range(rows-1, -1, -1):
        ans[rows-1-row][1] = ''.join(array[row][::-1])

    # 270도 출력
    for col in range(rows-1, -1, -1):
        for row in range(rows):
            ans[rows-1-col][2] += array[row][col]

    print("#", tc+1)
    for row in range(len(ans)):
        print(' '.join(ans[row]))
"""