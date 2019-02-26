"""
5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전
문제 내용
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.

최초 작성 2019.02.26 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190226_01_input.txt", "r")

T = int(input())
for tc in range(T):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    ans = M % N
    print("#{} {}".format(tc+1, numbers[ans]))

