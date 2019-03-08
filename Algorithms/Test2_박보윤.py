def findIsland(nextx, nexty):
    global maxvalue
    global N

    visited[nextx][nexty] = 1
    if maps[nextx][nexty] > maxvalue:
        maxvalue = maps[nextx][nexty]

    # 재귀 호출
    d1 = [-1, 0, 1, 0]
    d2 = [0, -1, 0, 1] # 상하좌우로 움직이기
    for direction in range(4):
        if 0 <= nextx+d1[direction] < N and 0 <= nexty+d2[direction] < N:
            if maps[nextx+d1[direction]][nexty+d2[direction]] >= 1 and visited[nextx+d1[direction]][nexty+d2[direction]] == 0: # 다음 길이 섬이고, 아직 안 간 길일 때
                findIsland(nextx+d1[direction], nexty+d2[direction])

T = int(input())
for tc in range(T):
    N = int(input()) # 지도의 크기
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    visited = [[0 for _ in range(N)] for __ in range(N)]
    # 모든 점을 시작점으로 잡고
    # visited가 아닌 경우 섬의 개수를 세면서 DFS 시작
    maxvalue = 0
    num = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 1 and visited[i][j] == 0: # 섬이고, 방문 안 했을 때,
                num += 1
                findIsland(i, j)

    print("#%d %d %d" %(tc+1, num, maxvalue))




    "서울2반박보윤 이름으로 제출"