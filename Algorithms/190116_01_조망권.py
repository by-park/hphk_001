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


최초 작성 2019.01.16 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190116_01_input.txt", "r")

# 1차 시도
"""
for i in range(10):
    numBuilding = int(input())
    Building_list = list(map(int, input().split()))
    good_house = 0
    for idx, building in enumerate(Building_list[2: -2]):
        if Building_list[idx + 1] >= building or Building_list[idx] >= building:
            left = 0
        else:
            left = min(building - Building_list[idx + 1], building - Building_list[idx])
        if Building_list[idx + 3] >= building or Building_list[idx + 4] >= building:
            right = 0
        else:
            right = min(building - Building_list[idx+3], building - Building_list[idx+4])
        good_house += min(left, right)
    print('#{0} {1}'.format(i+1, good_house))
"""

# 2차 시도
"""
for i in range(10):
    numBuilding = int(input())
    Building_list = list(map(int, input().split()))
    good_house = 0
    for idx, building in enumerate(Building_list[2: -2]):
        left = 0 if Building_list[idx + 1] >= building or Building_list[idx] >= building else min(building - Building_list[idx + 1], building - Building_list[idx])
        right = 0 if Building_list[idx + 3] >= building or Building_list[idx + 4] >= building else min(building - Building_list[idx+3], building - Building_list[idx+4])
        good_house += min(left, right)
    print('#{0} {1}'.format(i+1, good_house))
"""

# 3차 시도 - timebird7님 (max보다 sorted가 빠르다)
"""
for i in range(10):
    numBuilding = int(input())
    Building_list = list(map(int, input().split()))
    good_house = 0
    for idx in range(2, numBuilding-2):
        if Building_list[idx] == sorted(Building_list[idx-2:idx+3])[-1]:
            good_house += Building_list[idx] - sorted(Building_list[idx-2:idx+3])[-2]
    print('#{0} {1}'.format(i+1, good_house))
"""

# 4차 시도 - timebird7님 코드 변수 이름 변경
for i in range(10):
    n = int(input())
    B = list(map(int, input().split()))
    g = 0
    for j in range(2, n-2):
        if B[j] == sorted(B[j-2:j+3])[-1]:
            g += B[j] - sorted(B[j-2:j+3])[-2]
    print('#{0} {1}'.format(i+1, g))

# 코드 리뷰 - 강민수님 코드
for _ in range(10):
    t = int(range())
    l = list(map(int, input().split()))
    c = 0
    i = 2
    while i < t-2:
        max_ = sorted(l[i-2:i] + l[i+1:i+3])[-1]
        if l[i] > max_:
            c += l[i] - max_
            i += 3
        else:
            i += 1
    print(f'#{_+1} {c}')

# 선생님 코드 리뷰
def getMax(idx):
    tmax = heights[idx-2] # 처음 거는 걔가 맥스입니다.

    if tmax < heights[idx - 1]: tmax = heights[idx - 1] # 새로들어온 놈이 크면 맥스값 갱신
    if tmax < heights[idx + 1]: tmax = heights[idx + 1]
    if tmax < heights[idx + 2]: tmax = heights[idx + 2]

    return tmax

TC = 10
for tc in range(1, TC+1):

    N = int(input())
    heights = list(map(int, input().split()))
    view = 0 # 지금은 명확하지만 프로그램이 복잡해지면
    # init이라는 함수를 둬서 초기화를 해서 혹시나 이런 애들이
    # for문 위에 있지 않게 만든다.

    for i in range(2, N-2):
        side = getMax(i)
        if side < heights[i]: # Max보다 내가 더 크면
            view += heights[i] - side # 조망권이 확보된 것이므로 추가
    print("#%d %d" % (tc, view))


# visual studio는 실행시 ctrl + f5