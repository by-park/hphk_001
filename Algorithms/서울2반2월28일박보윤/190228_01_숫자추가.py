"""
5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가
문제 내용
N개의 10억 이하 자연수로 이뤄진 수열이 주어진다.
이 수열은 완성된 것이 아니라 M개의 숫자를 지정된 위치에 추가하면 완성된다고 한다.
완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.
다음은 숫자를 추가하는 예이다.
2 7 -> 2번 인덱스에 7을 추가하고 한 칸 씩 뒤로 이동한다.
4 8 -> 4번 인덱스에 8을 추가하고 한 칸 씩 뒤로 이동한다.

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
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190228_01_input.txt", "r")

T = int(input())

for tc in range(T):
    # input
    N, M, L = list(map(int, input().split()))
    numbers = input().split()
    for cnt in range(M):
        idx, num = input().split()
        numbers.insert(int(idx), num)
    print("#%d %s" %(tc+1, numbers[int(L)]))