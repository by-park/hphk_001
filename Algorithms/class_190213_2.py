# DFS 경로 출력
# 교재 연습 문제 3
# 2019.02.13 PBY

# 간선
lines = list(map(int,'1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))

visited = [0] * 7 # 1 부터 7까지

aMatrix = [[0 for _ in range(7)] for __ in range(7)]

stack = [0] * 100
top = 0

# 인접행렬 채우기
for idx in range(0, len(lines), 2):
    aMatrix[lines[idx]-1][lines[idx+1]-1] = 1
    aMatrix[lines[idx+1]-1][lines[idx]-1] = 1

# DFS 구현
# 시작 지점 방문
v = 1 # 시작지점


while not(all(visited)): # 모든 지점을 방문할 때까지 DFS를 돌린다.
    for i in range(7): # 방문 안한 w 찾기
        if aMatrix[v - 1][i] == 1 and visited[i] == 0:
            if stack[top-1] != v: # 이 체크를 안 하면 갔던 곳을 스택에 또 넣는다.
                stack[top] = v  # push
                visited[v - 1] = 1  # 방문 지점 체크
                print(v)
                top += 1  # 스택 포인트 증가 시작
            w = i + 1
            break
    else: w = -1

    while w != -1:
        # w가 존재하므로 w를 방문
        stack[top] = w
        visited[w-1] = 1
        top += 1
        print(w)

        # w를 방문했으니 w는 이제 출발 위치가 됨
        v = w

        # 방문 안한 w 찾기
        for i in range(7):
            if aMatrix[v - 1][i] == 1 and visited[i] == 0:
                w = i + 1
                break
        else: # w가 없다
            w = -1
    # while을 나왔다는 것은 더이상 갈 수 있는 depth가 없다는 것
    top -= 1
    v = stack[top-1]


# 방문 안한 w 하나만 찾아서 다시 그게 v가 되도록 한다.
# w를 체크


"""     
    # 아니 이건 BFS잖아
    wlist = []
    # v에서 인접 정점들 w를 다 찾아둔다. while로 구현하지 않고 for로 구현하기 위해 wlist에 따로 모아두었다.
    for i in range(100):
        if aMatrix[v-1][i] == 1:
            wlist.append(i+1)
    # 모든 w들을 다 방문한다.
    for i in range(len(wlist)):
        
    # v에서 인접 정점 w를 다 찾아둬야한다.
    # 그 w들을 다 넣고 (for로 해도 되는 거 아닌가)
    # w를 방문
    # 다음 방문 안한 w 찾기 - while문일 때만 필요한 부분
    # w가 없으면 v를 바꾼다.
    for idv in range(len(visited)):
        if visited[idv] == 0: # v의 인접 정점 중 방문 안한 w 찾기
            stack[top] = idv+1
            visited[idv] = 1
            top += 1
        while
#if not(all(visited)):

stack[top] = visited[0] # 방문하지 않은 곳?

# 지금 stack에 있는 곳을 기준으로
# 다음에 갈 곳을 인접행렬에서 찾는다.
for idx in aMatrix:
    aMatrix[][]
"""