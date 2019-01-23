""" 
1206. [S/W 문제해결 기본] 1일차 - View
문제 내용
시간 : 10개 테스트케이스를 합쳐서 C++의 경우 10초 / Java의 경우 20초 / Python의 경우 30초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내
※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.

A와 B로 표시된 세대의 경우는 왼쪽 조망은 2칸 이상 확보가 되었지만 오른쪽 조망은 한 칸 밖에 확보가 되지 않으므로 조망권을 확보하지 못하였다.
C의 경우는 반대로 오른쪽 조망은 2칸이 확보가 되었지만 왼쪽 조망이 한 칸 밖에 확보되지 않았다.
 
[제약 사항]
가로 길이는 항상 1000이하로 주어진다.
맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. (예시에서 빨간색 땅 부분)
각 빌딩의 높이는 최대 255이다.
 
[입력]
입력 파일의 첫 번째 줄에는 테스트케이스의 길이가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 조망권이 확보된 세대의 수를 출력한다.


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