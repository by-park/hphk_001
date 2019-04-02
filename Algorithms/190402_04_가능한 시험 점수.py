
"""
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1

답
7
11

bfs로 했을 때 틀린거 (가능한 반례)
1
9
10 9 8 7 6 5 6 7 8
59가 나와야하는데 57이 나온다.
2 3을 해서 5가 나온 것과 0 5를 해서 5가 나온 것을 구분하지 못하고 가지치기 할 수 있어서...?

dfs는 순열로 해서 그런지 틀리지 않는다.
"""


from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    max_ = sum(scores)+1
    numbers = [0] * (max_)
    numbers[0]=1; numbers[-1] = 1
    q = [0] #deque([0])
    cnt = -1
    ans = 2
    while q:
        lenq = len(q)
        cnt += 1
        if cnt >= N:
            break # while문 탈출
        for i in range(lenq): # 지금 Q에 있는 건 다 꺼내야함
            # 연산의 대상
            #a = q.popleft()
            a = q[i] # 꺼내지 않는다. q에 계속 append
            # a로부터 다음 갈 수 있는 애들 다 1로 바꾸기
            if a+scores[cnt] < max_:
                if numbers[a+scores[cnt]] == 0:
                    ans += 1
                    numbers[a+scores[cnt]] = 1
                    q.append(a+scores[cnt])


    print("#%d %d" %(tc, ans))

    
# 꽃몬님 도움
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    max_ = sum(scores)+1
    numbers = [0] * (max_)
    numbers[0]=1; numbers[-1] = 1
    for s in scores:
        temp = numbers[:]
        for i in range(max_):
            if temp[i] == 1:
                if i + s < max_:
                    numbers[i+s] = 1

    print("#%d %d" %(tc, sum(numbers)))
"""

# 왜지.... 32개로 맞아버렸다.
"""
def dfs(score, questions):
    global N, ns
    if questions == N+1: # 이거 왜 N일 때랑 N+1일 때랑 차이가 없지
        return
    
    for j in range(N):
        if perm[j] == False: # 아직 방문 안 했으면 거기서부터 dfs를 돌아서 가능한 경우의 수를 다 알아내도록
            if visited[score+scores[j]] == -1:
                visited[score+scores[j]] = questions + 1 # 하나 더 가는 것
                ns += 1
                perm[j] = True
                dfs(score+scores[j], questions+1)
                perm[j] = False
            elif visited[score+scores[j]] > questions + 1:
                visited[score+scores[j]] = questions+1 # 최소한으로 올 수 있는....
                perm[j] = True
                dfs(score+scores[j], questions+1)
                perm[j] = False

    
T= int(input())
for tc in range(1, T+1):
    N = int(input()) # 시험문제의 개수
    scores = list(map(int, input().split()))
    scores.sort() # 이걸 했는데, 제한 시간 초과가 났다.....
    maxvalue = sum(scores)
    visited = [-1] * (maxvalue+1)
    visited[0] = 1 # 빵점 가능
    visited[-1] = N # 최고점 가능
    ns = 2 # 가능한 시험 점수의 개수
    perm = [False] * N
    
    dfs(0, 0)

    print("#%d %d" %(tc, ns))
"""

# 메모리 초과
"""
from collections import deque
    
T= int(input())
for tc in range(1, T+1):
    N = int(input()) # 시험문제의 개수
    scores = list(map(int, input().split()))
    maxvalue = sum(scores)
    visited = [-1] * (maxvalue+1)
    visited[0] = 1 # 빵점 가능
    visited[-1] = N # 최고점 가능
    ns = 2 # 가능한 시험 점수의 개수
    perm = [False] * N
    # 시험 문제 하나씩 선택해서
    q = deque()
    for i in range(N):
        perm[i] = True
        if visited[scores[i]] == -1:
            visited[scores[i]] = 1
            ns += 1
        q.append([scores[i], 1, perm[:]]) # 선택한 것의 개수
        perm[i] = False
        
    while q:
        #print(q)
        score, num, perm = q.popleft()
        for i in range(N):
            if perm[i] == False and score + scores[i] < maxvalue:
                if visited[score+scores[i]] == -1:
                    visited[score+scores[i]] = num + 1
                    ns += 1
                    perm[i] = True
                    q.append([score+scores[i], num, perm[:]])
                    perm[i] = False
                elif visited[score+scores[i]] > num + 1:
                    visited[score+scores[i]] = num + 1
                    perm[i] = True
                    q.append([score+scores[i], num, perm[:]])
                    perm[i] = False
#    dfs(0, 0)

    print("#%d %d" %(tc, ns))
"""


# 이거를 dfs로 돌지 말고...
"""
def dfs(score, questions):
    global N, ns
    if questions == N+1: # 이거 왜 N일 때랑 N+1일 때랑 차이가 없지
        return
    
    for j in range(N):
        if perm[j] == False: # 아직 방문 안 했으면 거기서부터 dfs를 돌아서 가능한 경우의 수를 다 알아내도록
            if visited[score+scores[j]] == -1:
                visited[score+scores[j]] = questions + 1 # 하나 더 가는 것
                ns += 1
                perm[j] = True
                dfs(score+scores[j], questions+1)
                perm[j] = False
            elif visited[score+scores[j]] > questions + 1:
                visited[score+scores[j]] = questions+1 # 최소한으로 올 수 있는....
                perm[j] = True
                dfs(score+scores[j], questions+1)
                perm[j] = False

    
T= int(input())
for tc in range(1, T+1):
    N = int(input()) # 시험문제의 개수
    scores = list(map(int, input().split()))
    maxvalue = sum(scores)
    visited = [-1] * (maxvalue+1)
    visited[0] = 1 # 빵점 가능
    visited[-1] = N # 최고점 가능
    ns = 2 # 가능한 시험 점수의 개수
    perm = [False] * N
    
    dfs(0, 0)

    print("#%d %d" %(tc, ns))
"""

"""
# 무한 루프
def dfs(score, questions):
    global N
    if questions == N:
        return
    for j in range(N):
        if perm[j] == False: # 아직 방문 안 했으면 거기서부터 dfs를 돌아서 가능한 경우의 수를 다 알아내도록
#            if visited[score+scores[j]] == False:
            perm[j] = True # 지금까지의 합을 visited에 넣어줌
            visited[score+scores[j]] = True
            dfs(score+scores[j], questions+1)
            perm[j] = False

    
T= int(input())
for tc in range(1, T+1):
    N = int(input()) # 시험문제의 개수
    scores = list(map(int, input().split()))
    maxvalue = sum(scores)
    visited = [False] * (maxvalue+1)
    visited[0] = True # 빵점 가능
    visited[-1] = True # 최고점 가능
    perm = [False] * N
    
    dfs(0, 0)

    print("#%d %d" %(tc, sum(visited)))
"""


# 제한 시간 초과
"""
T= int(input())
for tc in range(1, T+1):
    N = int(input()) # 시험문제의 개수
    visited = [False] * (N * 100+1) # 각 문제에 최대 배점 100. 최고 점수까지 가능한 배열
    visited[0] = True # 0점도 가능
    scores = list(map(int, input().split()))

    # scores로 순열을 만들면서 가능한 점수인지 체크
    # 바이너리 카운팅
    for i in range(1<<N):
        # 그 문제에 대한 배점
        temp = 0
        for j in range(N):
            if i & (1<<j):
                # 배점 카운팅
                temp += scores[j]
        # 그렇게 계산되어 나온 temp가 시험 문제 개수
        visited[temp] = True
    print("#%d %d" %(tc, sum(visited)))
    
"""
