"""
5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
추가나 삭제가 없는 경우에는, 완전 이진 트리가 되도록 만들면 효율적인 이진 탐색 트리를 만들수 있다.
다음은 1부터 6까지의 숫자를 완전 이진 트리 형태인 이진 탐색 트리에 저장한 경우이다.
완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.


[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 N이 주어진다. 1<=N<=1000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

2019.03.04 PBY 최초작성
2019.03.05 최종제출
"""

import sys
sys.stdin = open('C:/Users/student/Documents/week2/day1/Algorithms/190305_02_input.txt', 'r')

# 재귀로 표현하기
def checkchild(start):
    global N
    if start*2 <= N:
        array[start][1] = start*2
        checkchild(start*2)
    if start*2+1 <= N:
        array[start][2] = start*2+1
        checkchild(start*2+1)

# 시작점은 1번 노드
def inorder(start):
    global n
    if start: #  and depth < maxdepth => 뎁스 정보는 필요가 없었다.... 위에서 미리 자식을 표시해두면 되는 거였다...
        inorder(array[start][1])
        array[start][0] = n
        n += 1
        inorder(array[start][2])

# 코드 구현            
T = int(input())
for tc in range(T):

    N = int(input())

    # 이 모양이 자세히 보니 inorder인 것 같다.

    array = [[0 for _ in range(3)] for __ in range(N+1)] # 내 값, 왼쪽 자식, 오른쪽 자식
    checkchild(1) # 1번부터 자식 있는 것까지 다 표시
        
    n = 1
    inorder(1)

    # 결과 출력
    print("#%d" %(tc+1),array[1][0], array[N//2][0])



"""
아래처럼 뎁스 구현하지 말고 재귀로 만들 것 => 성공!

    # 몇까지 있느냐에 따라 자식 노드가 있는지가 결정됨

    # 최대 뎁스
    i = 1; maxdepth = 0
    while True:
        if i < N:
            for i2 in range(i, i*2): # 1, 2~3 까지, 4~7까지
                if i2 == N: # 이렇게 풀면 안 되는데...
                    array[i2][1] = 1 # 오른쪽 자식이 없음
                else:
                    array[i2][1] = array[i2][2] = 1 # 왼쪽 오른쪽 자식이 있는 것처럼 채워줌
            i *= 2
        else: break
        maxdepth += 1

    # max depth만큼 자식 노드 넣기
"""
