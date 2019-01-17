""" 
4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

[문제 내용]
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

최초 작성 2019.01.17 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190117_03_input.txt", "r")


TC = int(input())

for i in range(TC):
    
    # input
    N = int(input())
    A = input()
    array = [0] * 10

    # 0~9 중에 몇 번 나왔는지 카운트
    for letter in A:
        array[int(letter)] += 1

    # max 찾기
    max_ = [0, array[0]]
    for idx, a in enumerate(array):
        if a >= max_[1] and idx > max_[0]:
            max_ = [idx, a]
    print("#{} {} {}".format(i+1, max_[0], max_[1])) 

