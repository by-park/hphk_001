""" 
4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

[문제 내용]
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
다음은 N=5, M=3이고 5개의 숫자 1 2 3 4 5가 배열 v에 들어있는 경우이다.
이웃한 M개의 합이 가장 작은 경우 1 + 2 + 3 = 6
이웃한 M개의 합이 가장 큰 경우 3 + 4 + 5 = 12
답은 12와 6의 차인 6을 출력한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

최초 작성 2019.01.17 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190117_04_input.txt", "r")


TC = int(input())

for i in range(TC):
    
    # input
    N, M = list(map(int, input().split()))
    v = list(map(int, input().split()))

    max_ = 0
    min_ = 9223372036854775807-1 # sys.maxsize - 1

    # 개수가 짝수인 경우 예외가 생김
    if M % 2 == 0:
        total_range = range(M//2, N-M//2+1)        
    else:
        total_range = range(M//2, N-M//2)

    for n in total_range:
        if M % 2 == 1:
            area = v[n - M//2: n + M//2+1]
        else:
            area = v[n - M//2: n + M//2]

        hap = 0
        for item in area:
            hap += item
        if hap > max_: 
            max_ = hap
        if hap < min_: 
            min_ = hap
    
    print("#{} {}".format(i+1, max_-min_))
    
# 짝수와 홀수를 이해 못해서....
# 이렇게 코드가 길어졌다....

# visual studio는 실행시 ctrl + f5
