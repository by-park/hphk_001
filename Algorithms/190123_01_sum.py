""" 
1206. [S/W 문제해결 기본] 2일차 - Sum
문제 내용
다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라. 

[제약 사항]
총 10개의 테스트 케이스가 주어진다.
배열의 크기는 100X100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
[입력]
각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.


최초 작성 2019.01.23 PBY
"""


# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190123_01_input.txt", "r")

TC = 10
for tc in range(TC):
    tnum = input()
    r=[]
    for _ in range(100):
        r.append(list(map(int,input().split())))
    
    # 행의 합
    rmax = 0
    for row in range(100):
        curs = 0
        for item in range(100):
            curs += r[row][item]
        if rmax < curs:
            rmax = curs

    # 열의 합
    cmax = 0
    for col in range(100):
        curs = 0
        for item in range(100):
            curs += r[item][col]
        if cmax < curs:
            cmax = curs

    # 대각선의 합
    curs = 0
    for d in range(100):
        curs += r[d][d]
    dmax = curs

    curs = 0
    for d in range(99, -1, -1):
        curs += r[d][d]
    if dmax < curs:
        dmax = curs

    # 행, 열, 대각선 합 최대값 비교
    if rmax >= cmax and rmax >= dmax:
        ans = rmax
    
    if cmax >= rmax and cmax >= dmax:
        ans = cmax

    if dmax >= cmax and dmax >= rmax:
        ans = dmax
    
    print("#{} {}".format(tc+1, ans))

    # 선생님 코드
    max = sum = 0
    for i in range(100):
        for j in range(100):
            sum += array[i][j]
        if max < sum : max = sum
        sum = 0
    
    for i in range(100):
        for j in range(100):
            sum += array[j][i] # i, j 위치를 바꾼다.
        if max < sum : max = sum
        sum = 0
    
    for i in range(100):
        sum += array[i][i]
    if max < sum: max= sum
    sum = 0

    for i in range(100):
        sum += array[i][99-i]
    if max < sum : max = sum
    
    print("#%d %d" %(tc, max))