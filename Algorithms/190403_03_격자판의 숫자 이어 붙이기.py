"""Solving Club"""
"""
격자판의 숫자 이어 붙이기

2019.04.03 PBY 최초작성

"""


# 덱으로 구현하려다가 그냥 visited없이 재귀로 간단하게 짜보려고 했다.
def go(x, y, cur, depth):
    if depth == 7:
        ans.append(cur)
        return
    # 동서남북 네 방향 가면서
    for d in range(4):
        if 0 <= x+dx[d] < 4 and 0<= y+dy[d] < 4: # 그냥 네 방향을 다 보내기
            go(x+dx[d], y+dy[d], cur+str(maps[x+dx[d]][y+dy[d]]), depth+1)

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for tc in range(1, T+1):
    maps = []
    for _ in range(4):
        maps.append(input().split())
    ans = []
    # 모든 점을 시작점으로 재귀를 돌도록 한다.
    for i in range(4):
        for j in range(4):
            go(i, j, str(maps[i][j]),1) # 지금 한 자리 선택한 거, 앞으로 6개 더 선택해서 7이 되면 끝
    print("#%d %d" %(tc, len(set(ans))))

# 매 시작점마다 visited를 만들어줘야하나.... => visited를 16으로 체크하면 되지 않나?
"""
from collections import deque
T = int(input())
for tc in range(1, T+1):
    maps = []
    for _ in range(4):
        maps.append(input().split())
    q = deque()
    # 매 점을 다 시작점으로 두면서
    for i in range(4):
        for j in range(4):
            q.append([i, j, str(maps[i][j])])
            while q:
                # 거기서 갈 수 있는

    # 그 시작점으로부터 4방향을 계속 이동해나감

    print("#%d %d" %(tc, len(set())))
"""