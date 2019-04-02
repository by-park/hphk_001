
"""

3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
"""

# 통과!
# 왜 통과지....
# 1) 방문 체크 한 것 그냥 통과해버린 문제
# 2) N-1, N-1일 때 멈추지 않고 계속 Q에 들어간 문제
# 3) min값으로 중간에 잘못된 가지치기

from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    # map을 완성했으면 시작점에서부터 큐를 돌면서 최소 비용을 저장해나감
    visited = [[False for _ in range(N)] for __ in range(N)]
    costs = [[1000*N*N for _ in range(N)] for __ in range(N)]
    visited[0][0]= True
    costs[0][0] = 0
    q = deque([[0, 0]]) # 시작점 들어감
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while q:
        #print(costs)
        x, y = q.popleft()
        #visited[x][y] = True
        for d in range(4):
            if 0<=x+dx[d]<N and 0<=y+dy[d] < N: # 판을 넘어서지 않고
                if maps[x+dx[d]][y+dy[d]] - maps[x][y] >= 0: # 높이가 더 높거나 인접
                        newcosts = maps[x+dx[d]][y+dy[d]] - maps[x][y] + 1
                else:
                        newcosts = 1
                if not visited[x+dx[d]][y+dy[d]] : # 아직 방문 안 해야 costs를 계산해서 업데이트
                    # costs 계산                    
                    visited[x+dx[d]][y+dy[d]] = True
                    costs[x+dx[d]][y+dy[d]] = costs[x][y] + newcosts
                    if x+dx[d] != N-1 or y+dy[d] != N-1:
                        q.append([x+dx[d], y+dy[d]])
                    # costs로 업데이트
                elif costs[x+dx[d]][y+dy[d]] > costs[x][y] + newcosts:# 방문했어도 costs가 더 작아질 수 있으면 다시 방문
                    costs[x+dx[d]][y+dy[d]] = costs[x][y] + newcosts
                    if x+dx[d] != N-1 or y+dy[d] != N-1:
                        q.append([x+dx[d], y+dy[d]])
                    
    print("#%d %d" %(tc, costs[N-1][N-1]))
    # visited를 해도
    
# 프림 알고리즘
# 매번 지금 연결된 간선 중 가장 최소의 길이를 가진 애로 뻗어나간다.
# 그러다가 도착점에 오면 stop
"""
# 뭘 잘못했는지 while문을 탈출 못함....
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    costs = [[1000*N*2 for _ in range(N)] for __ in range(N)]
    # 방문체크 따로 해야할 듯
    visited = [[False for _ in range(N)] for __ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    # 시작점에서 다음 지점으로 최소의 길을 찾음
    costs[0][0] = 0
    q = deque([[0, 0]])
    qlen = 1
    while q:
        print(q)
        print(costs)
        #print(costs)
        # 지금 나한테 연결된 간선 둘 중 최적의 간선을 찾을 것임
        minvalue = 1000*N*2
        check2 = 0
        for i in range(qlen):
            x, y = q.popleft()
            visited[x][y] = True
            qlen -= 1
            # 지금 지점에서 갈 수 있는 최단 비용 위치 찾기
            check = 0
            for d in range(4):
                nextx = x+dx[d]; nexty = y+dy[d]
                if 0 <= nextx < N and 0<= nexty < N and not visited[nextx][nexty]: # 다음 길이 판을 넘어서지 않고
                    newcost = abs(maps[x][y] - maps[nextx][nexty]) + 1 #최소 이동에 1은 걸린다.
                    check = 1 # visited 한 곳은 들어가지 않음
                    if newcost < minvalue: # 이걸 위에 붙여줘버려서 간선이 append가 되어버리지 않는 사태 발생...!
                        minvalue = newcost
                        mincost = costs[x][y] + newcost
                        mini = [nextx,nexty]
            if check == 1: # 간선이 있으면
                check2 = 1
                q.append([x,y])
                qlen += 1
            # 위치를 다 돌고 나면 최소의 간선을 찾아 들어감
        # for를 다 돌고 나면
        if check2 == 1:        
            costs[mini[0]][mini[1]] = mincost
            if mini[0] == N-1 and mini[1] == N-1: # 간선 찾았다고 break를 하면 안 되는 건가. 아직 다른 길도 있으니까?
                 continue # 최종점에서는 더 이상 이동하지 않는다.
            q.append(mini)
            qlen += 1
            # visit한 곳은 방문하지 않게 하려면 costs가 최소인 곳은 방문하지 않는다고 하면 되나?
        # 목적지에 도착하면 while문 탈출하기
    print("#%d %d" %(tc, costs[N-1][N-1]))
"""
    
# deque로 바꿔도 여전한 시간초과
"""
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    costs = [[1000*N*2 for _ in range(N)] for __ in range(N)]
    # map 시작점에서부터 BFS하면서 최소 비용 저장하기
    q = deque([[0, 0, 0]]) # 시작점 x, y, 최소비용
    costs[0][0] = 0 # 출발점은 비용이 0
    # 이동방향은 무조건 오른쪽이나 아래가 아닐 수 있다! 반례 가능. 지금 내가 온 길 말고 최소 길은 다 찾아야하는 듯 하다.
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    # 가지치기를 위한 min값이 필요한가?
    
    while q:
        # q를 다 돌았을 때 도착점에 있는 길이 정보를 return할 것이다.
        x, y, cur_cost = q.popleft()
        if x == N-1 and y == N-1: # 이 길이 도착점이면 더 이상 q를 돌아보지 않아도 된다.
            continue
        else:
            # 지금 길에서 다음 갈 수 있는 길 바꾸기
            for d in range(4):
                nextx = x+dx[d]; nexty = y+dy[d]
                if 0<=nextx < N and 0<= nexty < N: # 다음 길이 판을 넘어서지 않고
                    # 그 때의 코스트가 지금 오는 cost보다 작으면
                    newcost = abs(maps[x][y] - maps[nextx][nexty]) + 1 #최소 이동에 1은 걸린다.
                    if cur_cost + newcost < costs[nextx][nexty]:
                        costs[nextx][nexty] = cur_cost + newcost
                        # 최소 비용이 걸리는 곳이어야만 거기서 다음 길로 진행할 것임
                        # 이전에 한 번 방문했던 곳이라면 거기서 이미 큐가 진행되었을 테니 또 올 필요 없다.
                        if cur_cost+newcost > costs[N-1][N-1]: # min값을 이미 넘었으면 더 할 필요 없이 가지치기
                            continue
                        q.append([nextx, nexty, cur_cost+newcost])
    print("#%d %d" %(tc, costs[N-1][N-1]))
"""
          
# 가지치기를 해줄 수 있다!
# 지금 구해진 최소값보다 더 큰값이 나오고 있는 경우 아예 q에 넣지 않아도 된다.
# 시간초과로 4개까지 맞음
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    costs = [[1000*N*2 for _ in range(N)] for __ in range(N)]
    # map 시작점에서부터 BFS하면서 최소 비용 저장하기
    q = [[0, 0, 0]] # 시작점 x, y, 최소비용
    costs[0][0] = 0 # 출발점은 비용이 0
    # 이동방향은 무조건 오른쪽이나 아래가 아닐 수 있다! 반례 가능. 지금 내가 온 길 말고 최소 길은 다 찾아야하는 듯 하다.
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    # 가지치기를 위한 min값이 필요한가?
    
    while q:
        # q를 다 돌았을 때 도착점에 있는 길이 정보를 return할 것이다.
        x, y, cur_cost = q.pop(0)
        if x == N-1 and y == N-1: # 이 길이 도착점이면 더 이상 q를 돌아보지 않아도 된다.
            continue
        else:
            # 지금 길에서 다음 갈 수 있는 길 바꾸기
            for d in range(4):
                nextx = x+dx[d]; nexty = y+dy[d]
                if 0<=nextx < N and 0<= nexty < N: # 다음 길이 판을 넘어서지 않고
                    # 그 때의 코스트가 지금 오는 cost보다 작으면
                    newcost = abs(maps[x][y] - maps[nextx][nexty]) + 1 #최소 이동에 1은 걸린다.
                    if cur_cost + newcost < costs[nextx][nexty]:
                        costs[nextx][nexty] = cur_cost + newcost
                        # 최소 비용이 걸리는 곳이어야만 거기서 다음 길로 진행할 것임
                        # 이전에 한 번 방문했던 곳이라면 거기서 이미 큐가 진행되었을 테니 또 올 필요 없다.
                        if cur_cost+newcost > costs[N-1][N-1]: # min값을 이미 넘었으면 더 할 필요 없이 가지치기
                            continue
                        q.append([nextx, nexty, cur_cost+newcost])
    print("#%d %d" %(tc, costs[N-1][N-1]))
          
"""

# 런타임 에러
"""
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    costs = [[1000*N*2 for _ in range(N)] for __ in range(N)]
    # map 시작점에서부터 BFS하면서 최소 비용 저장하기
    q = [[0, 0] for _ in range(N*N**4)]
    front = -1; rear = 0
#    q = deque([[0, 0, 0]]) # 시작점 x, y, 최소비용
    costs[0][0] = 0 # 출발점은 비용이 0
    # 이동방향은 무조건 오른쪽이나 아래가 아닐 수 있다! 반례 가능. 지금 내가 온 길 말고 최소 길은 다 찾아야하는 듯 하다.
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while front != rear:
        # q를 다 돌았을 때 도착점에 있는 길이 정보를 return할 것이다.
        front += 1; x = q[front][0]; y = q[front][1]
        cur_cost = costs[x][y]
        # 지금 길에서 다음 갈 수 있는 길 바꾸기
        for d in range(4):
            nextx = x+dx[d]; nexty = y+dy[d]
            if 0<=nextx < N and 0<= nexty < N: # 다음 길이 판을 넘어서지 않고
                # 그 때의 코스트가 지금 오는 cost보다 작으면
                newcost = abs(maps[x][y] - maps[nextx][nexty]) + 1 #최소 이동에 1은 걸린다.
                if cur_cost + newcost <= costs[nextx][nexty]:
                    costs[nextx][nexty] = cur_cost + newcost
                    # 최소 비용이 걸리는 곳이어야만 거기서 다음 길로 진행할 것임
                    # 이전에 한 번 방문했던 곳이라면 거기서 이미 큐가 진행되었을 테니 또 올 필요 없다.
                    rear += 1; q[rear][0] = nextx; q[rear][1] = nexty
#                    q.append([nextx, nexty, cur_cost+newcost])
    print("#%d %d" %(tc, costs[N-1][N-1]))
"""
    
# 제한시간 초과
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    costs = [[1000*N*2 for _ in range(N)] for __ in range(N)]
    # map 시작점에서부터 BFS하면서 최소 비용 저장하기
    q = [[0, 0, 0]] # 시작점 x, y, 최소비용
    costs[0][0] = 0 # 출발점은 비용이 0
    # 이동방향은 무조건 오른쪽이나 아래가 아닐 수 있다! 반례 가능. 지금 내가 온 길 말고 최소 길은 다 찾아야하는 듯 하다.
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while q:
        # q를 다 돌았을 때 도착점에 있는 길이 정보를 return할 것이다.
        x, y, cur_cost = q.pop(0)
        # 지금 길에서 다음 갈 수 있는 길 바꾸기
        for d in range(4):
            nextx = x+dx[d]; nexty = y+dy[d]
            if 0<=nextx < N and 0<= nexty < N: # 다음 길이 판을 넘어서지 않고
                # 그 때의 코스트가 지금 오는 cost보다 작으면
                newcost = abs(maps[x][y] - maps[nextx][nexty]) + 1 #최소 이동에 1은 걸린다.
                if cur_cost + newcost <= costs[nextx][nexty]:
                    costs[nextx][nexty] = cur_cost + newcost
                    # 최소 비용이 걸리는 곳이어야만 거기서 다음 길로 진행할 것임
                    # 이전에 한 번 방문했던 곳이라면 거기서 이미 큐가 진행되었을 테니 또 올 필요 없다.
                    q.append([nextx, nexty, cur_cost+newcost])
    print("#%d %d" %(tc, costs[N-1][N-1]))
"""                


 
