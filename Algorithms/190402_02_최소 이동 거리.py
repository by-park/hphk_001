
"""
일방통행 구간!!!! =>  이거 때문에 계속 2개가 오답이 났다.
"""
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    N += 1
    ad = [[0 for _ in range(N)] for __ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        #ad[e][s] = w
    visited = [False]*N
    costs = [1000000*(N+1) for _ in range(N)] # 그 정점까지 올 때까지의 최소 거리
    # 연결 지점 번호 N과 도로의 개수 E가 주어진다.
    q = [0] # 0번 지점 시작점
    #visited[0] = True
    qlen = 1
    costs[0] = 0
    while q:
        for i in range(qlen):
            v = q.pop(0)
            qlen -= 1
            visited[v] = True
            for j in range(N):
                if visited[j] == False and 0 < ad[v][j]: # 갈 수 있는 연결된 간선들은 다 확인하는데,
                    if costs[v] + ad[v][j] < costs[j]: # 그렇게 이동하는게 이득일 때만 이동
                        costs[j] = costs[v] + ad[v][j]
                        if j != N-1: # 마지막 지점이면 더 들어가지 않음
                            q.append(j)
                            qlen += 1
    print("#%d %d" %(tc, costs[N-1]))
