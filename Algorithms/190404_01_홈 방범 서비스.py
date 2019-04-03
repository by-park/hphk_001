"""Solving Club"""
"""
홈 방범 서비스

2019.04.03 PBY 최초작성
"""

import sys
sys.stdin = open('190404_01_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 판때기 더 붙이기 # 최대 마름모만큼
    town = [[0] * (3*N) for _ in range(N)]
    for _ in range(N):
        temp = [0]*N + list(map(int, input().split())) + [0]*N
        town.append(temp)
    town.append([[0] * (3*N) for _ in range(N)])
    # 앞 뒤로 패딩 붙였으면, 이제 마름모를 가지고 돌면서 집 개수 확인하기
    # 가로로 최대 마름모 개수 x 세로로 최대 마름모 개수: 전체 길이 - 내 길이 +1
    # 마름모 시작점
    # 최대 마름모 크기: K*2-1
    # N을 하나 적은 홀수로 만들고 +1 / 2를 한다.
    if N % 2 == 0:
        K = N // 2
    else:
        K = (N+1) // 2
    size = K*2-1
    middle = [(K-1)*2, (K-1)*2] # 첫 중심
    maxhome = 0
    # 마름모 크기를 줄여 가면서
    for k in range(K, 0, -1):
        for i in range(3*k-size+1):
            middle[1] = (k-1)*2
            for j in range(3*k-size+1):
                # 그 시작점이 있으면 마름모 크기만큼
                home = 0
                for row in range(size):
                    home += sum(town[row][middle[1]-(k-1)*2 + abs(middle[0]-row):middle[1]+(k-1)*2-abs(middle[0]-row)])
                # 지금 마름모에 들어있는 home이
                middle[1] += j; middle[0] += i
                if home == 0: # 아무 집도 해당되지 않으면
                    continue
                if home * M >= k * k + (k - 1) * (k - 1) and home > maxhome:  # 손해를 내지 않으면
                    maxhome = home
        if maxhome > 0:
            break
    print(maxhome)



