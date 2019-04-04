"""Solving Club"""
"""
점심 식사시간

2019.04.04 PBY 최초작성
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    building = []
    for _ in range(N):
        building.append(list(map(int, input().split())))
    # 1은 사람 그 이외는 계단의 위치
    # stair1 위치찾기
    stairs = []
    for i in range(N):
        for j in range(N):
            if building[i][j] > 1:
                stairs.append([i, j])

