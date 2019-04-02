import sys
sys.stdin = open('190402_03_input.txt', 'r')
        
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 교실에 N명
    friends = [[0 for _ in range(N)] for __ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1][b-1] = 1
        friends[b-1][a-1] = 1

    nf = 0
    visited= [False] * N
    visited[0] = True # 상원이의 생일파티....니까 상원이 초대
    # 상원이의 친구들 초대
    invited_list = []
    for i in range(N):
        if friends[0][i] == 1:
            visited[i] = True # 초대장 주고
            invited_list.append(i)
            nf += 1
    # 친구들의 친구들을 다시 초대
    for i in invited_list:
        for j in range(N):
            if friends[i][j] == 1 and not visited[j]:
                visited[j] = True
                nf += 1
    print("#%d %d" %(tc, sum(visited)-1))

"""
# depth를 잘못 설정해서 나는 에러가 있다.... 2로 해도 틀리고, 3으로 해도 틀린다. 아예 구조가 틀렸다.
def invite(invited, depth):
    global nf
    if depth == 3:
        return
    # 친구를 찾아서 초대장을 보냄
    for i in range(N):
        if friends[invited][i] == 1 and visited[i] == False: # 둘이 친구인데 아직 초대장을 못 받았으면 보내줌
            visited[i] = True
            nf += 1 # 초대장 보낼 때 초대한 친구 수 늘림
            invite(i, depth+1)

        
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 교실에 N명
    friends = [[0 for _ in range(N)] for __ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1][b-1] = 1
        friends[b-1][a-1] = 1

    nf = 0
    visited= [False] * N
    visited[0] = True # 상원이의 생일파티....니까 상원이 초대
    invite(0, 0) # 상원이는 1번이니까 0과 연결된 애를 찾음
    print("#%d %d" %(tc, nf))
"""
