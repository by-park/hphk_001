"""
최소신장트리

3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

출력)
7
13
22

2019.04.01 PBY 최초작성
"""

# make set
# 가중치 w에 의해 정렬
# for로 가중치가 낮은 간선 들을 쭉 돌면서
# find set이 달라야만 들어간다.
# 들어가면 다시 union
"""
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V += 1 
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w
    # 간선 저장
    lines = [[0 for _ in range(V)] for __ in range(V)]

    ans = 0
    # 각각 인접을 보면서 가장 최소비용을 찾는 것을 다 저장
    # visited를 안 쓰면 방문한 간선을 한 번 더 더한다.
    visited = [False]*V
    start = 0
    # 인접 정점 중에서 방문을 하고 그 중 최소를 찾는다.
    for i in range(V):
#        if not visited[i]: # 방문 처리가 여기가 아님
            minvalue = 10
            check = 0
#            visited[i] = True # 방문 처리가 여기가 아니라
            for j in range(V):
                # 여기에 <= 를 안 써주면 안 된다!!!!!!! 최대가 10이니까!!!!!
                if 0 < ad[i][j] <= minvalue: # 연결된 게 하나도 없을 수 없으니까 하나는 minvalue가 나올 것
                    check = 1
                    minvalue = ad[i][j]
                    mini = j
                    # 나랑 연결된 간선도 visited가 끝난 것
            # minvalue 찾았으면
            if check == 1 and not lines[i][mini]:
                lines[i][mini] = 1
                lines[mini][i] = 1
#                visited[i] = True
                ans += minvalue
                #visited[mini] = True # 연결된 간선도 추가로 다시 나를 찾지 않게
    print("#%d %d" %(tc, ans))
"""    

# 예제 3개는 다 맞는데...반례를 못 찾겠다.

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V+=1
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w
    # 간선 저장
    lines = [[0 for _ in range(V)] for __ in range(V)]
    
    ans = 0
    # 각각 인접을 보면서 가장 최소비용을 찾는 것을 다 저장
    # visited를 안 쓰면 방문한 간선을 한 번 더 더한다.
    visited = [False]*V
    start = 0
    # 인접 정점 중에서 방문을 하고 그 중 최소를 찾는다.
    for i in range(V):
#        if not visited[i]: # 방문 처리가 여기가 아님
            minvalue = 10
            check = 0
#            visited[i] = True # 방문 처리가 여기가 아니라
            for j in range(V):
                # 여기에 <= 를 안 써주면 안 된다!!!!!!! 최대가 10이니까!!!!!
                if 0 < ad[i][j] <= minvalue: # 연결된 게 하나도 없을 수 없으니까 하나는 minvalue가 나올 것
                    check = 1
                    minvalue = ad[i][j]
                    mini = j
                    # 나랑 연결된 간선도 visited가 끝난 것
            # minvalue 찾았으면
            if check == 1 and not lines[i][mini]:
                lines[i][mini] = 1
                lines[mini][i] = 1
#                visited[i] = True
                ans += minvalue
                #visited[mini] = True # 연결된 간선도 추가로 다시 나를 찾지 않게
    print("#%d %d" %(tc, ans))



"""
from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V = V+1
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w

    # 각 시작점을 돌면서 탐색
    start = 0
    u = [10*V for _ in range(V)] # 최대값으로 넣어줌
    Q = [False]*V # False 중에서 최소를 찾도록
    u[start] = 0 # 시작 점은 거리가 0
#    q = deque(list(range(V)))
    q = deque([start])
    while q:
        vertex = q.popleft()
        Q[vertex] = True
        minvalue = 10*V

        check = 0
        for i in range(V):
            if not Q[i] and ad[vertex][i]!= 0:
                # 이게 원래 값보다 최소여야 업데이트 (이전에 방문했을 수 있다)
                #if u[vertex]+ad[vertex][i] < u[i]: # 최소값이 아니어서 들어온 거니까 무조건 바뀌어야한다.
                #u[i] = u[vertex]+ad[vertex][i] #최소값만 업데이트
                #q.append(i)
                if u[vertex]+ad[vertex][i] < minvalue:
                    minvalue = u[vertex]+ad[vertex][i]
                    minv = i
                    check = 1
        if check == 1:
            u[minv] = minvalue # 최소값만 업데이트
            q.append(minv)
        else: # 아직 방문 안한 곳 있으면 방문하라고
            for j in range(V):
                if not Q[j]:
                    q.append(j)
        #if check == 1:
        #    q.append(minv)
        
    #for i in range(V):
    #    if not Q[i] and ad[vertex][i]!=0:
    print(u[vertex])
    #print(Q)
    #print(u)
    ans = u[vertex]
"""

"""            
        ans = u[vertex]
        minvalue = 10*V
        for i in range(V):
            if not Q[i]:
                for j in range(V):
                    if 0 < ad[i][j] < minvalue:
                        minvalue = ad[i][j]
                # Q[i] 의 minvalue를 찾음
                Q[i] = True
                ans += minvalue
        print("#%d %d" %(tc, ans))
        return
    else:
        mst(minv)
"""
        
#    print("#%d %d" %(tc, minvalue))

"""
# Queue로 수정 직전
def mst(vertex):
    global V
    Q[vertex] = True
    # 인접한 것들 최소 계산
    minvalue = 10*V
    check = 0
    print(Q)
    for i in range(V):
        if not Q[i] and ad[vertex][i]!= 0:
            #if u[i] > u[vertex] + ad[vertex][i]: # 새로 방문하는게 의미가 있을 때만
            u[i] = u[vertex]+ad[vertex][i]
            check = 1
            if u[i] < minvalue:
                minvalue = u[i]
                minv = i
    if check == 0: # 다음에 들어갈 게 없으면
#        print(u[vertex])
#        print(Q)
        # False인 애들만 돌면서 최소 찾기
        ans = u[vertex]
        minvalue = 10*V
        for i in range(V):
            if not Q[i]:
                for j in range(V):
                    if 0 < ad[i][j] < minvalue:
                        minvalue = ad[i][j]
                # Q[i] 의 minvalue를 찾음
                Q[i] = True
                ans += minvalue
        print("#%d %d" %(tc, ans))
        return
    else:
        mst(minv)


from collections import deque

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V = V+1
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w

    # 각 시작점을 돌면서 탐색
    start = 0
    u = [10*V for _ in range(V)] # 최대값으로 넣어줌
    Q = [False]*V # False 중에서 최소를 찾도록
    u[start] = 0 # 시작 점은 거리가 0

    q = deque([start])
    while q:
        vertex = q.popleft()
        
    mst(start)
        
#    print("#%d %d" %(tc, minvalue))
"""

# Queue를 쓰지 않으면 안 되는 것 같다.
"""
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V+=1
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w

    ans = 0
    # 각각 인접을 보면서 가장 최소비용을 찾는 것을 다 저장
    # visited를 안 쓰면 방문한 간선을 한 번 더 더한다.
    visited = [False]*V
    for i in range(V):
#        if not visited[i]: # 방문 처리가 여기가 아님
            minvalue = 10
            check = 0
#            visited[i] = True # 방문 처리가 여기가 아니라
            for j in range(V):
                if not visited[j] and 0 < ad[i][j] < minvalue: # 연결된 게 하나도 없을 수 없으니까 하나는 minvalue가 나올 것
                    check = 1
                    minvalue = ad[i][j]
                    mini = j
                    # 나랑 연결된 간선도 visited가 끝난 것
            # minvalue 찾았으면
            if check == 1:
                visited[i] = True
                ans += minvalue
                #visited[mini] = True # 연결된 간선도 추가로 다시 나를 찾지 않게
    print("#%d %d" %(tc, ans))
"""


#이것도 모든 간선이 연결이 안 된 3 번 케이스를 틀린다.
"""
def mst(vertex):
    global V
    Q[vertex] = True
    # 인접한 것들 최소 계산
    minvalue = 10*V
    check = 0
    for i in range(V):
        if not Q[i] and ad[vertex][i]!= 0:
            #if u[i] > u[vertex] + ad[vertex][i]: # 새로 방문하는게 의미가 있을 때만
            u[i] = u[vertex]+ad[vertex][i]
            check = 1
            if u[i] < minvalue:
                minvalue = u[i]
                minv = i
    if check == 0: # 다음에 들어갈 게 없으면
        print(u[vertex])
        return
    else:
        mst(minv)
    
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V = V+1
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w

    # 각 시작점을 돌면서 탐색
    start = 0
    u = [10*V for _ in range(V)] # 최대값으로 넣어줌
    Q = [False]*V # False 중에서 최소를 찾도록
    u[start] = 0
    mst(start)
        
#    print("#%d %d" %(tc, minvalue))
"""

# 모든 간선이 연결된 게 아니기 때문에 이런 식으로 돌면 마지막 케이스는 아예 답을 찾을 수 없다.
"""
def mst(vertex, cur_sum):
    print(vertex)
    global minvalue, V
    visited[vertex] = True
    minweight = 10; minv = 0
    check = 0
    for i in range(V):
        if  ad[vertex][i]!=0 and ad[vertex][i] < minweight and not visited[i]: # 아예 연결이 안 되어있으면 가중치가 0이다.
            minweight = ad[vertex][i]
            minv = i
            check = 1
            
    if check == 0: # 다음에 들어갈 게 없으면
        if sum(visited) == V and cur_sum < minvalue: # 전체 다 방문한게 아니면 안 됨
            minvalue = cur_sum
        return
    # 그 최소값을 가지고 들어감
    else:
        mst(minv, cur_sum+minweight)
    
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    V = V+1
    minvalue = 10*V
    ad = [[0 for _ in range(V)] for __ in range(V)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad[s][e] = w
        ad[e][s] = w

    # 각 시작점을 돌면서 탐색
    for i in range(V):
        visited = [False]*V
        mst(i, 0)
        
    print("#%d %d" %(tc, minvalue))
"""
