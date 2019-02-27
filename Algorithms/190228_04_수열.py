"""
5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집
문제 내용
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다. 이 수열은 완성된 것이 아니라 M번의 편집을 거쳐 완성된다고 한다.
완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.
다음은 미완성 수열과 편집의 예이다.
I 2 7 -> 2번 인덱스 앞에 7을 추가하고, 한 칸 씩 뒤로 이동한다.
D 4 -> 4번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동한다.
C 3 8 -> 3번 인덱스 자리를 8로 바꾼다.
만약 편집이 끝난 후 L이 존재하지 않으면 -1을 출력한다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.
그 다음 M개의 줄에 걸쳐 추가할 인덱스와 숫자 정보가 주어진다. 5<=N<=1000, 1<=M<=1000, 6<=L<=N+M

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.02.27 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190228_04_input.txt", "r")

T = int(input())

for tc in range(T):
    # input
    N, M, L = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    for _ in range(M):
        # query = input()
        query = input().split()

        # if int(query[2]) > len(numbers)-1: # 접근할 수 없는 경우
        #     numbers=[]
        #     break # 끝내버리기

        if query[0] == "I": # Insert 구현
            # numbers.insert(int(query[2]), int(query[4]))
            numbers.insert(int(query[1]), int(query[2]))
        elif query[0] == "D": # Delete 구현
            # numbers.pop(int(query[2]))
            numbers.pop(int(query[1]))
        elif query[0] == "C": # 교환 구현 여기 else로 써서 런타임 에러인가...
            # numbers[int(query[2])] = int(query[4])
            numbers[int(query[1])] = int(query[2])

    # 편집이 끝난 후 L이 존재하지 않으면 -1
    if L > len(numbers) - 1:
        print("#%d -1" %(tc+1))
    else:
        print("#%d %d" %(tc+1, numbers[L]))

"""
런타임 에러
혹시 인덱스가 맞지 않는 경우가 있나?
=> test case 중에 빈칸 2 개 들어온 경우 있다!!!!!!!!!!!!
I  2 3 이런 식
그래서 인풋 받을 때 반드시 split을 해줘야한다.
"""