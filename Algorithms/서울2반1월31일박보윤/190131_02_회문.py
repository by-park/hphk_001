""" 
4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
문제 내용
BBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.01.31 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190131_02_input.txt", "r")

testcase = int(input())
for tc in range(1, testcase+1):
    N, M = list(map(int, input().split()))

    # 회문 찾을 판 만들기 (input)
    pan = []
    for _ in range(N):
        pan += [input()]
    palin = ''

    # 가로를 돌면서 M에 해당하는 회문 찾기
    checkk1, checkj1 = -1, -1
    for i1 in range(N):

        # 가로 한 줄 안에서 시작점을 잡고
        for j1 in range(N-M+1):

            # 시작점 안에서 길이만큼 검사한다. (최대 길이 = 회문의 절반길이)
            for k in range(j1, j1+M//2):

                # 회문이 아닌 경우 바로 다음 시작점 검사하도록 break
                if pan[i1][k] != pan[i1][-N+M-1+j1-k+j1]: # -1 -(N-M) 으로 뒷 자리 정하고 j1을 더해서 시작점만큼 뒤로 밀어주고 현재 검사중인 k가 시작점에서 얼마나 떨어졌는지(k-j1)로 회문 안으로 점점 좁혀가게 만든다.
                    palin = ''
                    break
                else:  # 회문일 가능성이 있는 경우 계속 추적
                    palin += pan[i1][k]

                    # 그러다가 회문을 찾은 경우
                    if len(palin) == M//2:
                        checkk1, checkj1 = 0, 0
                        break
            if checkk1 == 0: break # 회문을 찾은 경우 for문 나가기
        if checkj1 == 0: break


    # 세로를 돌면서 M에 해당하는 회문 찾기
    checkk2, checkj2 = -1, -1
    for i2 in range(N):

        # 세로 한 줄 안에서 시작점을 잡고
        for j2 in range(N-M+1):

            # 시작점 안에서 길이만큼 검사한다.(최대길이 = 회문의 절반길이)
            for k in range(j2, j2+M//2):

                # 회문이 아닌 경우 바로 다음 시작점 검사하도록 break
                if pan[k][i2] != pan[-N+M-1+j2-k+j2][i2]:
                    palin = ''
                    break
                else:  # 회문일 가능성이 있는 경우 계속 추적
                    palin += pan[k][i2]

                    # 그러다가 회문을 찾은 경우
                    if len(palin) == M // 2:
                        checkk2, checkj2 = 0, 0
                        break
            if checkk2 == 0: break
        if checkj2 == 0: break

    # 출력
    print("#%d " % tc, end="")
    if checkj1 == 0: # 가로찾다가 break 나온 경우
        for num in range(M):
            print(pan[i1][j1+num], end = "")
        print()
    if checkj2 == 0: # 세로찾다가 break 나온 경우
        for num in range(M):
            print(pan[j2+num][i2], end = "")
        print()



# pycharm은 실행시 alt+shift+f10 (이전 파일 또 실행 shift+f10)
# visual studio는 실행시 ctrl + f5
