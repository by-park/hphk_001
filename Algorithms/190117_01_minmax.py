""" 
4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

[문제 내용]
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


최초 작성 2019.01.17 PBY
"""

# 제출 시 삭제할 부분
import sys
sys.stdin = open("C:/Users/student/Documents/week2/day1/Algorithms/190117_01_input.txt", "r")

# 1차 시도
TC = int(input())
for i in range(TC):
    SC = int(input())
    S = list(map(int, input().split()))

    # Bubble Sort
    for j in range(SC, 0, -1):
        for index in range(j-1):
            if S[index] >= S[index+1]:
                S[index], S[index+1] = S[index+1], S[index]
    print('#{} {}'.format(i, S[-1] - S[0]))        

# visual studio는 실행시 ctrl + f5

# 선생님 코드
# 선형 자료구조이고 개수가 들어온다.
def find(a, n):
    # 이 문제는 value가 중요하기 때문에 index 사용하는 대신 value를 직접 받아가면서 했다.
    max_value = a[0]
    min_value = a[0]
    
    # 하나씩 추가하면서 비교하겠다. 어차피 끝까지 가니까 max, min을 동시에 비교해도 된다.
    for i in range(1, n):
        
        # max값보다 더 크면 max값을 갱신
        if a[i] > max_value:
            max_value = a[i]
        # 반대 개념도 min값보다 작으면 min값을 갱신
        if a[i] < min_value:
            min_value = a[i]
        
    # 그 차이를 반환하면 답
    return max_value - min_value