"""
5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

2019.03.04 PBY 최초작성
"""

import sys
sys.stdin = open('C:/Users/student/Documents/week2/day1/Algorithms/190305_01_input.txt', 'r')


def preorder(start):
    global cnt
    if start:
        preorder(array[start][0])
        preorder(array[start][1])
        cnt += 1


T = int(input())
for tc in range(T):

    # 간선의 개수 E, 루트 N
    E, N = list(map(int, input().split()))

    # 부모와 자식 노드 쌍 (노드 번호는 E+1까지 존재)
    array = [[0 for _ in range(2)] for __ in range(E+2)]
    lines = list(map(int, input().split()))
    for idx in range(0, len(lines), 2):
        if array[lines[idx]][0]:
            array[lines[idx]][1] = lines[idx+1]
        else:
            array[lines[idx]][0] = lines[idx+1]

    # 루트부터 순회하면서 존재하는 자식 노드 카운트
    cnt = 0
    preorder(N)

    # 결과 출력
    print("#%d %d" %(tc+1, cnt))
