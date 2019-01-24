""" 
4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.
짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
예를 들어 책이 총 400쪽이면, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 중간 페이지 c= int((l+r)/2)로 계산한다.
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
A는 300, B는 50 쪽을 찾아야 하는 경우, 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
테스트 케이스 별로 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, A, B, 0 중 하나를 출력한다.

최초 작성 2019.01.24 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190124_03_input.txt", "r")

testcase = int(input())
for tc in range(testcase):
    P, A, B = list(map(int, input().split()))

    # 이진탐색 알고리즘 (책의 페이지니까 검색 실패는 없음)
    # A입장에서
    s, e = 1, P
    acnt = 0
    while s <= e:
        c = int((s+e)/2)
        acnt += 1
        if c == A:  # A를 찾았다.
            break
        elif c > A:
            e = c
        else:
            s = c

    # B입장에서
    s, e = 1, P
    bcnt = 0
    while s <= e:
        c = int((s+e)/2)
        bcnt += 1
        if c == B:  # B를 찾았다.
            break
        elif c > B:
            e = c
        else:
            s = c

    
    # 더 빠른 사람을 출력
    if acnt < bcnt:
        print("#%d A" % (tc+1))
    elif acnt > bcnt:
        print("#%d B" % (tc+1))
    else:
        print("#%d 0" % (tc+1))

# 10개중 8개 맞음 - e = c-1, s = c+1로 했더니 잘못된 경우 발생
# 문제의 예제에서 e=c, s=c로 업데이트했기 때문에 그것을 따른 후 패스

# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
