""" 
[S/W 문제해결 기본] 3일차 - 회문2
문제 내용
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
위와 같은 글자 판이 주어졌을 때, 길이가 가장 긴 회문은 붉은색 테두리로 표시된 7칸짜리 회문이다.
예시의 경우 설명을 위해 글자판의 크기가 100 x 100이 아닌 8 x 8으로 주어졌음에 주의한다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
총 10개의 테스트케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 길이를 출력한다.

최초 작성 2019.01.31 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190131_05_input.txt", "r")

for tc in range(1, 11):
    tn = input()

    # 회문 판 만들기
    # strlist = [input() for _ in range(N)]
    pan = []
    for num in range(100):
        pan += [input()]

    # 세로도 전치해서 붙여서 가로처럼 찾기
    pan2 = ['' for _ in range(100)]
    for row in range(100):
        for col in range(100):
            pan2[row] += pan[col][row]
    pan += pan2

    # 제일 긴 거부터 찾아서 break로 나오기
    maxv = 0
    for length in range(100, 0, -1):
        # 매 행을 다 돌면서
        for row in range(len(pan)):
            # 시작점을 하나 잡고
            for startpoint in range(0, 100-length+1):
                # 그 안에 지금 정한 길이만큼 회문 검사
                for check in range(length): # -1 뒤에서부터 -(100-len) 회문 길이 까지 오고, start로 뒤로 밀기 그리고 -check로 회문 점점 좁혀가기
                    if pan[row][startpoint+check] != pan[row][-100+length-1+startpoint-check]:
                        break # 회문 가능성 없으면 바로 break
                #  for문을 다 돌았으면 회문이므로 max값을 체크한다.
                if check == length-1:
                    maxv = length
            if maxv > 0: break # max를 찾은 경우 for문 다 나오기
        if maxv > 0: break

    print("#%d %d" %(tc, maxv))


# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
