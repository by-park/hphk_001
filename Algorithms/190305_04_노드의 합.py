"""
5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
[문제]
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.
다음은 리프 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.
N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음단계의 왼쪽부터 시작된다.
완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.
리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 다음, 지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성 하시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L이 주어지고, 다음 줄부터 M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
 
2019.03.05 PBY 최초작성
"""

import sys
sys.stdin = open('C:/Users/student/Documents/week2/day1/Algorithms/190305_04_input.txt', 'r')


T = int(input())
for tc in range(T):

    # 인풋
    N, M, K = list(map(int, input().split()))

    # 완전이진트리
    q = [0 for i in range(N+1)]

    for _ in range(M):
        # 인풋을 받고 해당 위치에 넣어줌
        nodeid, nodeitem = list(map(int, input().split()))
        q[nodeid] = nodeitem

    # 뒤에서부터 오면서 합을 구하기?
    # 끝 수가 짝수인 경우(=이진트리 마지막에 형제노드가 없는 경우)는 해당 부모 노드에 그냥 그 값을 넣어준다.
    if N % 2 == 0:
        q[N//2] = q[N] # 이 부분에 nodeid랑 nodeitem을 쓸 수 있는 줄 알고 실수 => 항상 마지막 노드가 마지막 인풋인 게 아니기 때문에 그러면 절대 안 된다.
        N -= 1
        
    while N > 1: # 1인 경우는 부모 노드가 없다.
        q[N//2] = q[N] + q[N-1]
        N -= 2 # 노드 두 개의 합을 계산했으니 두 칸씩 이동함

    # K번째 노드에 들어있는 값 출력
    print("#%d %d" %(tc+1,q[K]))
    
